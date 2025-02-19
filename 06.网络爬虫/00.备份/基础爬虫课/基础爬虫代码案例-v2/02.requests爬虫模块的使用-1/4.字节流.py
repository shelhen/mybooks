# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 下午9:41
# @Author  : 顾安
# @File    : 4.字节流.py
# @Software: PyCharm

import requests

"""
requests支持使用字节流的方式下载大型文件
"""
url = 'https://www.baidu.com'

response = requests.get(url, stream=True)

with open('1.html', 'wb') as f:
    for chunk in response.iter_content(chunk_size=100):
        f.write(chunk)


"""
1. 当代码走到14行执行识不会直接发送请求, 走到iter_content才会发送请求并获取内容
2. get方法请求卡顿
"""
