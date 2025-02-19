# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.内容回顾-使用xpath获取豆瓣电影评论信息.py
# @Software: PyCharm
# @Time    : 2023/10/29 20:34


import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
}


url = 'https://movie.douban.com/subject/1292052/comments?status=P'

response = requests.get(url, headers=headers).text


tree = etree.HTML(response)

div_list = tree.xpath('//div[@class="comment-item "]')

# div_list中的每一个元素对象都包含对应的span标签
for content in div_list:
    print(content.xpath('.//span[@class="short"]/text()'))




