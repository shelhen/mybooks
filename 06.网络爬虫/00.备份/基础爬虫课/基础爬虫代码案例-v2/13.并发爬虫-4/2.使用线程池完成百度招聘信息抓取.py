# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.使用线程池完成百度招聘信息抓取.py
# @Software: PyCharm
# @Time    : 2023/11/14 21:00


import time
import pymysql
import requests
from concurrent.futures import ThreadPoolExecutor


class BaiDuWork:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', db='py_spider')
        self.cursor = self.db.cursor()
        self.api_url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Cookie': 'BAIDUID_BFESS=C53383C20F6054BA564E26C8F8A5936B:FG=1; Hm_lvt_50e85ccdd6c1e538eb1290bc92327926=1699966855; RT="z=1&dm=baidu.com&si=ff14b8e4-11b2-42be-beec-23fef6d5ad62&ss=loycdetx&sl=1&tt=1qt&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_50e85ccdd6c1e538eb1290bc92327926=1699966881',
            'Referer': 'https://talent.baidu.com/jobs/social-list?search=python'
        }

    def __del__(self):
        self.cursor.close()
        self.db.close()

    def get_work_info(self, page):
        post_data = {
            'recruitType': 'SOCIAL',
            'pageSize': 10,
            'keyWord': 'python',
            'curPage': page,
            'projectType': ''
        }

        response = requests.post(self.api_url, headers=self.headers, data=post_data)
        return response

    def parse_work_info(self, response):
        work_list = response.json()['data']['list']
        for work_info in work_list:
            education = work_info['education'] if work_info['education'] else '空'
            name = work_info['name']
            service_condition = work_info['serviceCondition']
            self.save_work_info(education, name, service_condition)

    def create_table(self):
        sql = """
            create table if not exists baidu_work_pool(
                id int primary key auto_increment,
                education varchar(200),
                name varchar(100),
                service_condition text
            );
        """
        try:
            self.cursor.execute(sql)
            print('表创建成功...')
        except Exception as e:
            print('表创建失败:', e)

    def save_work_info(self, education, name, service_condition):
        sql = """
            insert into baidu_work_pool(id, education, name, service_condition) values (
                %s, %s, %s, %s
            )
        """
        try:
            self.cursor.execute(sql, (0, education, name, service_condition))
            self.db.commit()
            print('数据保存成功...')
        except Exception as e:
            print('数据保存失败:', e)
            self.db.rollback()

    def main(self):
        self.create_table()
        with ThreadPoolExecutor(max_workers=5) as pool:
            future_list = list()
            for page in range(1, 6):
                response = pool.submit(self.get_work_info, page)
                future_list.append(response)

            for item in future_list:
                self.parse_work_info(item.result())


if __name__ == '__main__':
    baidu_work = BaiDuWork()
    baidu_work.main()
