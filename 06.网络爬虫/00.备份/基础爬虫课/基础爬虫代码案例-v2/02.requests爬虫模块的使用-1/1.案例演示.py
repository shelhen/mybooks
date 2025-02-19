# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 下午9:11
# @Author  : 顾安
# @File    : 1.案例演示.py
# @Software: PyCharm


import requests


"""
使用requests发送网络请求
    百度
"""

# 1. 定义访问的网址
url = 'https://www.baidu.com'

# 2. 使用requests发送get请求
response = requests.get(url)

# 3. 打印接收的对象
print(response)

# 4. 查看response对象的属性
print(response.status_code)  # 响应状态码
print(response.content)  # 获取当前网站的页面源代码[字节]
print('-' * 50)
print(response.text)  # 获取网站返回的页面源代码[字符串]

print('-' * 50)

# 将字节数据转为字符串数据 python中decode默认的解码方式为utf8
print(response.content.decode())

print('-' * 50)

# 获取当前请求头
print(response.request.headers)
print('-' * 50)

# 获取响应头
print(response.headers)
print('-' * 50)

# 获取cookie
# print(response.request.cookies)
# print('-' * 50)

# 获取set-cookie信息
print(response.cookies)

# 获取访问的url地址
print(response.url)










