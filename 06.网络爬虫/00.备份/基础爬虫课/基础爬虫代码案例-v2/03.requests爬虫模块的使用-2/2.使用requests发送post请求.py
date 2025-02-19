# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午8:21
# @Author  : 顾安
# @File    : 2.使用requests发送post请求.py
# @Software: PyCharm


import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'http://www.cninfo.com.cn/new/disclosure'

data = {
    'column': 'szse_latest',
    'pageNum': 1,
    'pageSize': 30,
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true'
}

response = requests.post(url, headers=headers, data=data)
print(response.json())


"""
1.判断目标网站是否是一个动态网站
2.如果是动态网站则使用浏览器开发者工具获取数据接口
3.观察当前接口的请求方式，如果是post请求则查看载荷数据
4.构造表单数据并使用requests发送post请求
"""

