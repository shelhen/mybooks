# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午8:57
# @Author  : 顾安
# @File    : 5.重定向与历史请求.py
# @Software: PyCharm

import requests


headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

# response = requests.get('https://www.360buy.com/', headers=headers, allow_redirects=False)
# print(response.url)

"""
默认情况下，requests发送的请求方式除了get、post、head、options，get和post都可以完成自动跳转的功能
可以让当前请求禁止跳转: allow_redirects=False
"""

response = requests.get('https://www.360buy.com/', headers=headers)
# 获取历史请求信息
# print(response.history)
for info in response.history:
    # info.headers是响应头
    print(info.status_code, info.url, info.headers)
