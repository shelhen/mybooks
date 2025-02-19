# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午9:44
# @Author  : 顾安
# @File    : 10.session会话.py
# @Software: PyCharm


import requests


# 1. 创建一个session对象
session = requests.Session()


# 2. 创建一个headers
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

# 3. 使用session对象发送请求
response = session.get('https://www.baidu.com', headers=headers)
print('第一次请求的请求头为:', response.request.headers)
print('响应头:', response.headers)
print('服务器设置的cookie为:', requests.utils.dict_from_cookiejar(response.cookies))

# 4.第二次请求时会携带服务器设置的set-cookie中的值
response = session.get('https://www.baidu.com')
print(response.request.headers.get('Cookie'))



