# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.内容回顾-使用bs4完成搜狗文章信息提取.py
# @Software: PyCharm
# @Time    : 2023/10/29 20:55

import requests
from bs4 import BeautifulSoup

url = 'https://weixin.sogou.com/weixin?_sug_type_=1&type=2&query=python'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
}


response = requests.get(url, headers=headers).text

# 1. 创建soup对象
soup = BeautifulSoup(response, 'lxml')

# 当前返回的是列表类型
# 此列表中的元素只有一个 ul
ul_tag = soup.select('ul[class=news-list]')

h3_list = ul_tag[0].select('h3')

for temp in h3_list:
    print(temp.select('a')[0].text)
    print(temp.select('a')[0].get('href'))




