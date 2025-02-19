# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.亚马逊爬虫案例.py
# @Software: PyCharm
# @Time    : 2023/11/26 21:44


"""
conda创建环境的指令:
    1.查询存在的虚拟环境
        conda info -e

    2.conda create -n 虚拟环境名称 python=版本号
"""
import threading
import time
import pymysql
import requests
import retrying  # pip install retrying
from lxml import etree
from queue import Queue
from loguru import logger  # 日志包: pip install loguru

# 在下载当前框架时一定要确保当前环境是一个新的虚拟环境
from feapder.network.user_agent import get  # UA池


class AmazonShop:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', db='py_spider')
        self.cursor = self.db.cursor()

        self.amazon_api = 'https://www.amazon.cn/nav/ajax/hamburgerMainContent?ajaxTemplate=hamburgerMainContent&pageType=Gateway&hmDataAjaxHint=1&navDeviceType=desktop&isSmile=0&isPrime=0&isBackup=false&hashCustomerAndSessionId=284d1b5a4086d9d81cafe4e0cdb784184a5c9f92&languageCode=zh_CN&environmentVFI=AmazonNavigationCards%2Fdevelopment-nov13patch%40B6165608796-AL2_x86_64&secondLayerTreeName=apparel_shoes%2Bcomputer_office%2Bhome_kitchen%2Bbeauty_pca%2Bsports_outdoor%2Bgrocery%2Bbaby_toy%2Bphones_elec%2Bjewelry_watch%2Bhome_improvement%2Bvideo_game%2Bmusical_instrument%2Bcamera&customerCountryCode=null'

        self.headers = {
            "Referer": "https://www.amazon.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "downlink": "10",
            "ect": "4g",
            "rtt": "200",
        }

        # 商品分类地址队列
        self.classify_url_queue = Queue()
        # 商品详情地址队列
        self.detail_url_queue = Queue()
        # 商品数据队列
        self.shop_info_queue = Queue()

    """数据表创建"""

    def create_table(self):
        sql = """
            create table if not exists amazon_shop(
                id int primary key auto_increment,
                price varchar(255) not null,
                title varchar(255) not null,
                goods_url varchar(255) not null
            );
        """

        try:
            self.cursor.execute(sql)
            print('商品表创建成功...')
        except Exception as e:
            print(f'商品表创建失败:', e)

    """访问分类api并返回api中的分类数据"""

    @retrying.retry(stop_max_attempt_number=3)
    def get_shop_data(self, url):
        self.headers['User-Agent'] = get()
        response = requests.get(url, headers=self.headers)
        return response

    """在api数据中提取一级分类标题一级商品列表中的node参数"""

    def get_classify_info(self):
        try:
            response = self.get_shop_data(self.amazon_api).json()['data']
            tree = etree.HTML(response)
            li_list = tree.xpath('//ul/li[position() > 2]')
            for li in li_list:
                item = dict()
                if li.xpath('./a/text()'):
                    if '全部' in li.xpath('./a/text()')[0]:
                        continue

                    if 'http' in li.xpath('./a/@href')[0]:
                        continue

                    item['title'] = li.xpath('./a/text()')[0]
                    item['href'] = li.xpath('./a/@href')[0].split('=')[1].split('&')[0]
                    # print(item)
                    self.classify_url_queue.put(item)
        except Exception as e:
            print('请求失败:', e)
            logger.error('请求失败的链接:', self.amazon_api)

    """根据node参数构造商品列表页并提取商品列表也中的详情页地址"""

    def get_detail_url(self):
        while True:
            info_url = self.classify_url_queue.get()
            try:
                response = self.get_shop_data('https://www.amazon.cn/s?rh=n%3A' + info_url['href'] + '&fs=true').text
            except Exception as e:
                print('访问失败:', e)
                logger.error('商品列表页访问失败:', 'https://www.amazon.cn/s?rh=n%3A' + info_url['href'] + '&fs=true')
                continue

            tree = etree.HTML(response)
            if tree.xpath('//span[@class="s-pagination-strip"]/span[last()]/text()'):
                max_page = tree.xpath('//span[@class="s-pagination-strip"]/span[last()]/text()')[0]
                # 根据在商品列表页中提取的最大页数进行翻页
                for page in range(1, int(max_page) + 1):
                    new_page = 'https://www.amazon.cn/s?rh=n%3A' + info_url['href'] + '&fs=true&page=' + str(page)
                    try:
                        response = self.get_shop_data(new_page)
                    except Exception as e:
                        print('访问失败:', e)
                        logger.error('商品列表页访问失败:', new_page)
                        continue

                    tree = etree.HTML(response.text)
                    # 获取所有指定商品的详情地址
                    detail_href_list = tree.xpath('//div[@class="sg-col-inner"]/span/div[1]/div/div/div//h2/a/@href')
                    for detail_href in detail_href_list:
                        item = dict()
                        item['detail_href'] = detail_href
                        # print('成立:', item)
                        self.detail_url_queue.put(item)
            else:
                page = 'https://www.amazon.cn/s?rh=n%3A' + info_url['href'] + '&fs=true'
                response = self.get_shop_data(page)
                tree = etree.HTML(response.text)
                # 获取所有指定商品的详情地址
                detail_href_list = tree.xpath('//div[@class="sg-col-inner"]/span/div[1]/div/div/div//h2/a/@href')
                for detail_href in detail_href_list:
                    item = dict()
                    item['detail_href'] = detail_href
                    # print('不成立:', item)
                    self.detail_url_queue.put(item)

            self.classify_url_queue.task_done()

    """访问商品详情页并完成数据提取"""

    def parse_shop_info(self):
        while True:
            detail_url_dict = self.detail_url_queue.get()
            detail_url = 'https://www.amazon.cn/' + detail_url_dict['detail_href']

            try:
                response = self.get_shop_data(detail_url)
            except Exception as e:
                print('访问失败:', e)
                logger.error('详情页访问失败:', detail_url)
                continue

            tree = etree.HTML(response.text)

            # 商品标题
            title = tree.xpath('//div[@id="centerCol"]//h1/span/text()')[0] if tree.xpath(
                '//div[@id="centerCol"]//h1/span/text()') else tree.xpath('//title/text()')[0]

            # 商品价格
            if tree.xpath('//div[@id="centerCol"]//div[@id="apex_desktop"]//span[@class="a-price-whole"]/text()'):
                price = "￥" + tree.xpath(
                    '//div[@id="centerCol"]//div[@id="apex_desktop"]//span[@class="a-price-whole"]/text()')[0]
            else:
                price = '-'.join(tree.xpath(
                    '//td[@class="a-span12"]//span[@class="a-offscreen"]/text()'))

            print(title.strip(), price)
            # 将解析到的商品数据打包成一个元组提交到队列中
            self.shop_info_queue.put((title.strip(), price, detail_url))
            self.detail_url_queue.task_done()

    """商品数据保存"""

    def save_shop_info(self):
        while True:
            # 定义列表用于数据的批量存储
            info_list = list()

            # 在队列中连续取到30条数据并添加到info列表中
            for _ in range(30):
                info = self.shop_info_queue.get()
                info_list.append((0,) + info)
                self.shop_info_queue.task_done()

            sql = """
                insert into amazon_shop(id, title, price, goods_url) values (
                    %s, %s, %s, %s
                );
            """

            try:
                # 批量保存, executemany接收的是一个迭代对象
                self.cursor.executemany(sql, info_list)
                self.db.commit()
                print('数据插入成功:', info_list)
            except Exception as e:
                print('数据插入失败:', e)
                logger.error('数据库保存失败:', e)
                self.db.rollback()

    """启动函数"""

    def main(self):
        self.create_table()

        # 创建线程对象列表
        thread_list = list()

        # 分类线程
        thread_list.append(threading.Thread(target=self.get_classify_info))

        # 商品详情
        for _ in range(10):
            thread_list.append(threading.Thread(target=self.get_detail_url))

        # 数据解析
        for _ in range(2):
            thread_list.append(threading.Thread(target=self.parse_shop_info))

        # 数据保存 一定要确保只有一个子线程在完成这个功能
        thread_list.append(threading.Thread(target=self.save_shop_info))

        for thread_obj in thread_list:
            thread_obj.daemon = True
            thread_obj.start()

        # 延迟等待子线程对象启动
        time.sleep(4)

        for queue in [self.classify_url_queue, self.detail_url_queue, self.shop_info_queue]:
            queue.join()


if __name__ == '__main__':
    # 日志记录:文件过大于500M就会重新生成一个文件
    logger.add('runtime_{time}.log', rotation='500 MB')
    amazon_shop = AmazonShop()
    amazon_shop.main()
