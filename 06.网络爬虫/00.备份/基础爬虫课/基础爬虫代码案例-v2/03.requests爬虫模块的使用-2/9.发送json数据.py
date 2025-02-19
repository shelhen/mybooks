# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午9:38
# @Author  : 顾安
# @File    : 9.发送json数据.py
# @Software: PyCharm


import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

response = requests.get('https://fanyi.baidu.com/sug', headers=headers, json={'kw': 'python'}, timeout=3)
print(response.request.headers)
print(response.request.body)

