# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午9:26
# @Author  : 顾安
# @File    : 7.请求超时.py
# @Software: PyCharm

import requests


# 如果某些网站响应时间过程应该设置超时时间让程序抛出异常
# 否则可能会让当前爬虫项目卡死
response = requests.get('https://www.google.com', timeout=2)
print(response)
