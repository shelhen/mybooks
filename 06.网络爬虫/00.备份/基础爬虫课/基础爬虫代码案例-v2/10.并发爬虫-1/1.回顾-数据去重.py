# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.回顾-数据去重.py
# @Software: PyCharm
# @Time    : 2023/11/7 20:08


import redis
import pymongo
import hashlib
import requests


class MovieInfo:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        self.api_url = 'https://pianku.api.mgtv.com/rider/list/pcweb/v3'

        self.mongo_client = pymongo.MongoClient()
        self.collection = self.mongo_client['py_spider']['mg_info']
        self.redis_client = redis.Redis()

    # 请求数据
    def get_movie_info(self, params):
        response = requests.get(self.api_url, headers=self.headers, params=params).json()
        return response

    # 数据清洗以及数据结构调整
    def parse_movie_data(self, response):
        movie_list = response['data']['hitDocs']
        for movie in movie_list:
            item = dict()
            item['title'] = movie['title']
            item['subtitle'] = movie['subtitle']
            item['story'] = movie['story']
            self.save_movie_info(item)

    # 数据去重
    @staticmethod
    def get_md5(item):
        md5_hash = hashlib.md5(str(item).encode('utf-8')).hexdigest()
        return md5_hash

    # 数据保存
    def save_movie_info(self, item):
        value = self.get_md5(item)
        # 当前集合的key如果有冒号, redis会在内部创建一个文件夹
        result = self.redis_client.sadd('movie:filter', value)

        # 如果md5可以正确保存到redis中则返回1, 否则返回0
        if result:
            self.collection.insert_one(item)
            print('保存成功: ', item)
        else:
            print('数据重复...')

    # 启动方法
    def main(self):
        for page in range(1, 3):
            params = {
                "allowedRC": "1",
                "platform": "pcweb",
                "channelId": "2",
                "pn": page,
                "pc": "80",
                "hudong": "1",
                "_support": "10000000",
                "kind": "19",
                "area": "10",
                "year": "all",
                "chargeInfo": "a1",
                "sort": "c2"
            }
            response = self.get_movie_info(params)
            self.parse_movie_data(response)


if __name__ == '__main__':
    movie_info = MovieInfo()
    movie_info.main()
