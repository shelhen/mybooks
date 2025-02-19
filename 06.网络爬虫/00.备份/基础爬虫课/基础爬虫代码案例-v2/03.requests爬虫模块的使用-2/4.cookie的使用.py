# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午8:51
# @Author  : 顾安
# @File    : 4.cookie的使用.py
# @Software: PyCharm


import requests


url = 'https://www.baidu.com'

response = requests.get(url)
# 获取到响应头中的cookie
print(response.cookies)


# 提取cookie信息的两种方式
cookie = response.cookies
print(dict(cookie))

cookie = requests.utils.dict_from_cookiejar(response.cookies)
print(cookie)




