# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.作业_阿里招聘.py
# @Software: PyCharm
# @Time    : 2023/11/5 20:13


import pymysql
import requests


class ALiWork:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', db='py_spider')
        self.cursor = self.db.cursor()

        self.api_url = 'https://talent.taotian.com/position/search?_csrf=079413f1-edaa-45e5-bbd8-7340f3a6df6c'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Cookie': "cna=yny1HZ86bg8CAXH2a4H1B55y; xlly_s=1; prefered-lang=zh; XSRF-TOKEN=079413f1-edaa-45e5-bbd8-7340f3a6df6c; SESSION=MkIzMjYxQzhEMTlBREE1ODEwRkVGMTMwRDMwQkVFQUI=; isg=BNDQizKWgRQC3F0U02P1enFWoRgimbTjKOSTDMqkWysfBXWvc63bcRF03c3l1Wy7"
        }

    # 获取数据
    def get_work_info(self):
        for page in range(1, 11):
            json_data = {
                "channel": "group_official_site",
                "language": "zh",
                "batchId": "",
                "categories": "",
                "deptCodes": [],
                "key": "",
                "pageIndex": page,
                "pageSize": 10,
                "regions": "",
                "subCategories": ""
            }

            response = requests.post(self.api_url, headers=self.headers, json=json_data).json()
            yield response['content']['datas']

    # 解析数据
    def parse_work_info(self, response):
        for work_info_list in response:
            for work_info in work_info_list:
                item = dict()
                item['categories'] = work_info['categories'][0] if work_info['categories'] else '空'
                item['work_name'] = work_info['name']
                item['description'] = work_info['description']
                print(item)

                # 数据解析完成之后需要调用其他的实例方法完成保存任务
                self.insert_work_info(0, item['categories'], item['work_name'], item['description'])

    # 创建数据表
    def create_table(self):
        sql = """
            create table if not exists ali_work(
                id int primary key auto_increment,
                categories varchar(20),
                work_name varchar(100),
                work_desc text
            );
        """

        try:
            self.cursor.execute(sql)
            print('表创建成功...')
        except Exception as e:
            print('表创建失败: ', e)

    # 数据保存
    def insert_work_info(self, *args):
        sql = """
            insert into ali_work(
                id,
                categories,
                work_name,
                work_desc
            ) values (%s, %s, %s, %s);
        """

        try:
            self.cursor.execute(sql, args)
            self.db.commit()
            print('数据插入成功...')
        except Exception as e:
            print('数据插入失败: ', e)
            self.db.rollback()

    # 启动函数
    def main(self):
        self.create_table()
        all_work_generator_object = self.get_work_info()
        self.parse_work_info(all_work_generator_object)


if __name__ == '__main__':
    ali_work = ALiWork()
    ali_work.main()


