# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.结合mongodb完成爱奇艺数据采集.py
# @Software: PyCharm
# @Time    : 2023/11/5 21:31


import pymongo
import requests


class AiQiYi:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(host='localhost', port=27017)
        self.collection = self.mongo_client['py_spider']['AiQiYi']

        self.api_url = 'https://pcw-api.iqiyi.com/search/recommend/list'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        }

    # 获取数据
    def get_movie_info(self, params):
        response = requests.get(self.api_url, headers=self.headers, params=params).json()
        return response

    # 数据解析
    def parse_movie_info(self, response):
        category_movies = response['data']['list']
        for movie in category_movies:
            item = dict()
            item['title'] = movie['title']
            item['playUrl'] = movie['playUrl']
            item['description'] = movie['description']
            self.save_movie_info(item)
            print('保存成功:', item)

    # 数据保存
    def save_movie_info(self, item):
        self.collection.insert_one(item)

    # 启动方法
    def main(self):
        for page in range(1, 6):
            params = {
                'channel_id': '2',
                'data_type': '1',
                'mode': '11',
                'page_id': page,
                'ret_num': '48',
                'session': 'df4d98969318544574e8d13e45b4999d',
                'three_category_id': '15;must',

            }

            response = self.get_movie_info(params)
            self.parse_movie_info(response)


if __name__ == '__main__':
    aqy = AiQiYi()
    aqy.main()
