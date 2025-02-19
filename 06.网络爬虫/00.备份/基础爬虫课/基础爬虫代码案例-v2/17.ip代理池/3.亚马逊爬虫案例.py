# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.亚马逊爬虫案例.py
# @Software: PyCharm
# @Time    : 2023/11/26 21:44


"""
conda创建环境的指令:
    1.查询存在的虚拟环境
        conda info -e

    2.conda create -n 虚拟环境名称 python=版本号
"""

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

        # 付费代理api地址, 需要替换自己购买的代理地址
        # self.ip_url = ''

        """
        创建队列对象
        """
        # self.ip_queue = Queue()

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
