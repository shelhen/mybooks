# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.使用多进程完成芒果视频信息抓取.py
# @Software: PyCharm
# @Time    : 2023/11/14 21:40


import time
import redis
import pymongo
import hashlib
import requests
from multiprocessing import Process, JoinableQueue as Queue


class MgMovieInfo:
    # 在多进程中, 对于数据库初始化操作必须设置为类属性
    mongo_client = pymongo.MongoClient()
    collection = mongo_client['py_spider']['mg_movie_process']
    redis_client = redis.Redis()

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        self.api_url = 'https://pianku.api.mgtv.com/rider/list/pcweb/v3'

        self.params_queue = Queue()
        self.json_queue = Queue()
        self.content_queue = Queue()

    # 构造查询字符串数据
    def get_params(self):
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
            self.params_queue.put(params)

    # 发送请求
    def get_movie_info(self):
        while True:
            params = self.params_queue.get()
            response = requests.get(self.api_url, headers=self.headers, params=params).json()
            self.json_queue.put(response)
            self.params_queue.task_done()

    # 数据清洗
    def parse_info(self):
        while True:
            response = self.json_queue.get()
            movie_list = response['data']['hitDocs']
            for movie in movie_list:
                item = dict()
                item['title'] = movie['title']
                item['subtitle'] = movie['subtitle']
                item['story'] = movie['story']
                self.content_queue.put(item)
            self.json_queue.task_done()

    # 获取对应字典的md5的值
    @staticmethod
    def get_md5(value):
        md5_hash = hashlib.md5(str(value).encode('utf-8')).hexdigest()
        return md5_hash

    def save_movie_info(self):
        while True:
            item = self.content_queue.get()
            value = self.get_md5(item)
            result = self.redis_client.sadd('movie:filter', value)
            if result:
                self.collection.insert_one(item)
                print('保存成功:', item)
            else:
                print('数据重复...')
            self.content_queue.task_done()

    def main(self):
        # 创建一个进程对象列表
        process_obj_list = list()

        # 创建一个进程对象用于构造查询字符串并将对象添加到进程列表中
        p_params = Process(target=self.get_params)
        process_obj_list.append(p_params)

        for _ in range(3):
            p_get_movie = Process(target=self.get_movie_info)
            process_obj_list.append(p_get_movie)

        p_save = Process(target=self.save_movie_info)
        process_obj_list.append(p_save)

        for p in process_obj_list:
            p.daemon = True
            p.start()

            # 进程启动需要消耗大量时间
            time.sleep(0.3)

        for q in [self.params_queue, self.json_queue, self.content_queue]:
            q.join()

        print('主进程结束...')


if __name__ == '__main__':
    movie_info = MgMovieInfo()
    movie_info.main()
