# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.bs4中的解析方法-根据标签字符串解析.py
# @Software: PyCharm
# @Time    : 2023/10/26 21:44

from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 当前string基本不用

soup = BeautifulSoup(html, 'lxml')

# 当前返回的是对应标签的文本值
res_1 = soup.find_all(string='Elsie')
print(res_1)

res_2 = soup.find_all(string=['Elsie', 'Lacie', 'Tillie'])
print(res_2)


