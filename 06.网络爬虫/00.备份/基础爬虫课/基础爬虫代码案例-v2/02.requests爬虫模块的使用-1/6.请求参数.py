# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 下午9:57
# @Author  : 顾安
# @File    : 6.请求参数.py
# @Software: PyCharm

import requests


# url = 'https://www.baidu.com/s'
#
# 1. 设置查询字符串关键字
# kw = {'wd': 'python'}
#
# 2. 请求指定地址并携带查询字符串
# response = requests.get(url, params=kw)
#
# 3. 查询请求的url
# print(response.url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

url = 'https://www.baidu.com/s?wd=python'
response = requests.get(url, headers=headers)
print(response.content.decode())

