# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.json数据的转换.py
# @Software: PyCharm
# @Time    : 2023/10/24 20:07

import json
import requests

url = 'http://www.cninfo.com.cn/new/disclosure'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 '
                  'Safari/537.36 Edg/109.0.1280.54'
}


post_data = {
    'column': 'szse_latest',
    'pageNum': 1,
    'pageSize': 30,
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true'
}

response = requests.post(url, headers=headers, data=post_data).content.decode()

# 是将字符转为字典对象
json_dict = json.loads(response)
print(type(json_dict))

# 将字典对象转为字符串
byte_data = json.dumps(json_dict)
# print(byte_data)


json_data = requests.post(url, headers=headers, data=post_data).json()
print(type(json_data))





