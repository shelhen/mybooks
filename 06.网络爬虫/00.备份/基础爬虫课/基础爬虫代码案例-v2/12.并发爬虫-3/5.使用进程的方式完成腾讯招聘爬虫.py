# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.使用进程的方式完成腾讯招聘爬虫.py
# @Software: PyCharm
# @Time    : 2023/11/11 21:38


import time
import pymongo
import requests
import jsonpath
from multiprocessing import Process, JoinableQueue as Queue
# from concurrent.futures import ProcessPoolExecutor

url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def get_work_info_json(page_num, queue):
    params = {
        'timestamp': 1696774900608,
        'countryId': '',
        'cityId': '',
        'bgIds': '',
        'productId': '',
        'categoryId': '',
        'parentCategoryId': '',
        'attrId': '',
        'keyword': 'python',
        'pageIndex': page_num,
        'pageSize': 10,
        'language': 'zh-cn',
        'area': 'cn'
    }

    response = requests.get(url, headers=headers, params=params).json()
    for info in response['Data']['Posts']:
        work_info_dict = dict()
        work_info_dict['recruit_post_name'] = jsonpath.jsonpath(info, '$..RecruitPostName')[0]
        work_info_dict['country_name'] = jsonpath.jsonpath(info, '$..CountryName')[0]
        work_info_dict['location_name'] = jsonpath.jsonpath(info, '$..LocationName')[0]
        work_info_dict['category_name'] = jsonpath.jsonpath(info, '$..CategoryName')[0]
        work_info_dict['responsibility'] = jsonpath.jsonpath(info, '$..Responsibility')[0]
        work_info_dict['last_update_time'] = jsonpath.jsonpath(info, '$..LastUpdateTime')[0]
        print(work_info_dict)
        queue.put(work_info_dict)


def save_work_info(queue):
    mongo_client = pymongo.MongoClient()
    collection = mongo_client['py_spider']['tx_work']

    while True:
        dict_data = queue.get()
        print(dict_data)
        collection.insert_one(dict_data)

        # 将当前队列中的计数器减1, 如果队列计数器为0, 则接堵塞, 可以直接退出主程序
        queue.task_done()


if __name__ == '__main__':
    # 进程是必须要创建函数入口的
    dict_data_queue = Queue()

    # 创建进程对象列表
    process_list = list()

    for page in range(1, 51):
        p_get_info = Process(target=get_work_info_json, args=(page, dict_data_queue))
        process_list.append(p_get_info)

    p_save_work = Process(target=save_work_info, args=(dict_data_queue,))
    process_list.append(p_save_work)

    for process_obj in process_list:
        process_obj.daemon = True
        process_obj.start()

    # 开启进程需要消耗大量的时间
    time.sleep(3)

    dict_data_queue.join()  # 如果队列中的计数器不为零则会堵塞主程序
    print('主程序退出...')


