# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.使用多线程完成爱奇艺电影数据提取.py
# @Software: PyCharm
# @Time    : 2023/11/14 20:05


import time
import pymongo
import requests
import threading
from queue import Queue


class AiQiYi:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(host='localhost', port=27017)
        self.collection = self.mongo_client['py_spider']['Thread_AiQiYi']

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Referer': 'https://list.iqiyi.com/www/2/15-------------11-1-1-iqiyi--.html?s_source=PCW_SC'
        }

        self.api_url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=2&data_type=1&mode=11&page_id={}&ret_num=48&session=765d98595c9c4b86535814ffedaf7fca&three_category_id=15;must'

        # 创建队列
        self.url_queue = Queue()
        self.json_queue = Queue()
        self.content_dict_queue = Queue()

    def get_url(self):
        for page in range(1, 6):
            time.sleep(1)
            self.url_queue.put(self.api_url.format(page))

    def get_api_json(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            # print(response.json())
            self.json_queue.put(response.json())
            self.url_queue.task_done()

    def parse_movie_info(self):
        while True:
            json_data = self.json_queue.get()
            category_movies = json_data['data']['list']
            for movie in category_movies:
                item = dict()
                item['title'] = movie['title']
                item['playUrl'] = movie['playUrl']
                item['description'] = movie['description']
                self.content_dict_queue.put(item)
            self.json_queue.task_done()

    def save_movie_info(self):
        while True:
            item = self.content_dict_queue.get()
            self.collection.insert_one(item)
            print('插入成功:', item)
            self.content_dict_queue.task_done()

    def main(self):
        # 创建线程对象列表
        thread_obj_list = list()

        # 创建获取url的线程对象并加入到线程对象列表中
        t_url = threading.Thread(target=self.get_url)
        thread_obj_list.append(t_url)

        # 创建发送请求的多个线程对象并添加到线程列表中
        for _ in range(3):
            t_get_json = threading.Thread(target=self.get_api_json)
            thread_obj_list.append(t_get_json)

        # 创建解析数据的线程对象并添加到线程对象列表中
        t_parse_info = threading.Thread(target=self.parse_movie_info)
        thread_obj_list.append(t_parse_info)

        # 创建保存数据的线程对象并添加到线程对象列表中
        t_save_info = threading.Thread(target=self.save_movie_info)
        thread_obj_list.append(t_save_info)

        for t_obj in thread_obj_list:
            t_obj.daemon = True
            t_obj.start()

        # 当前所有的队列对象中的计数器为零才能解堵塞主程序
        for q in [self.url_queue, self.json_queue, self.content_dict_queue]:
            q.join()

        print('主程序结束...')


if __name__ == '__main__':
    aqy = AiQiYi()
    aqy.main()
