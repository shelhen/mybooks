# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 下午9:31
# @Author  : 顾安
# @File    : 2.页面编码.py
# @Software: PyCharm


import requests

url = 'https://www.baidu.com'

response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)
