# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.腾讯爬虫-数据库保存.py
# @Software: PyCharm
# @Time    : 2023/11/2 21:01


import pymysql
import requests


class TxWork:
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1698929979279&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=1&keyword=python&pageIndex={}&pageSize=10&language=zh-cn&area=cn'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }

    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='root', db='py_spider')
        self.cursor = self.db.cursor()

    def __del__(self):
        # 当这个类的生命周期为del退出时, 会触发__del__方法
        self.cursor.close()
        self.db.close()

    # 获取数据 当前方法是一个生成器函数, 所以调用后会返回一个生成器对象
    @classmethod
    def get_work_info(cls):
        for page in range(1, 11):
            response = requests.get(cls.url.format(page), cls.headers).json()
            print(f'正在获取第{page}页')
            work_list = response['Data']['Posts']
            yield work_list

    # 创建表
    def create_table(self):
        sql = """
            create table if not exists tx_work(
                id int primary key auto_increment,
                work_name varchar(100) not null,
                country_name varchar(50),
                city_name varchar(50),
                work_desc text
            );
        """
        try:
            self.cursor.execute(sql)
            print('表创建成功...')
        except Exception as e:
            print('表创建失败:', e)

    # 数据录入
    def insert_work_info(self, *args):
        """
        :param args:
            id
            work_name
            country_name
            city_name
            work_desc
        :return:
        """
        sql = """
            insert into tx_work(
                id,
                work_name,
                country_name,
                city_name,
                work_desc
            ) values (%s, %s, %s, %s, %s);
        """
        try:
            self.cursor.execute(sql, args)
            self.db.commit()
            print('数据插入成功...')
        except Exception as e:
            print('数据插入失败:', e)
            # 事务回滚
            self.db.rollback()
        # 当前数据库连接不能关闭, 第一页保存完成后还需要保存第二页
        # finally:
        #     self.db.close()

    def main(self):
        self.create_table()
        all_work_generator_object = self.get_work_info()
        # mysql中的主键是自增长的, 需要使用0占位主键位置让主键数据自动生成
        work_id = 0
        for work_info_list in all_work_generator_object:
            for work_info in work_info_list:
                work_name = work_info['RecruitPostName']
                country_name = work_info['CountryName']
                city_name = work_info['LocationName']
                work_desc = work_info['Responsibility']
                self.insert_work_info(work_id, work_name, country_name, city_name, work_desc)


tx_work = TxWork()
tx_work.main()


# 作业: 获取阿里招聘的岗位信息
# 地址: https://talent.taotian.com/off-campus/position-list?lang=zh
