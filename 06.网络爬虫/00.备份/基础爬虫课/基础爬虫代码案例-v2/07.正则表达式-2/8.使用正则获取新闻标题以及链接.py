# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.使用正则获取新闻标题以及链接.py
# @Software: PyCharm
# @Time    : 2023/10/31 21:00


import re
import requests

url = 'https://m.36kr.com'

# 伪装safari移动端浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                  "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}

response = requests.get(url, headers=headers).text

# href="([^"]*): 去除页面中链接的双引号
item_list = re.findall(r'<a class="item-info clearfloat" href="([^"]*).*?ellipsis-2">(.*?)</span>.*?</a>', response)
for temp in item_list:
    print(url + temp[0], temp[1])


r'[^\d]'


