# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.bs4中的解析方法-attr解析.py
# @Software: PyCharm
# @Time    : 2023/10/26 21:39


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


soup = BeautifulSoup(html, "lxml")

res_1 = soup.find_all(attrs={'class': 'sister'})
print(res_1)
res_2 = soup.find_all(class_='sister')
print(res_2)

res_3 = soup.find_all(id='link2')
print(res_3)



