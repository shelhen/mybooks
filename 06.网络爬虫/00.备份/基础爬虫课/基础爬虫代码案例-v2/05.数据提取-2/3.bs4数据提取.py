# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.bs4数据提取.py
# @Software: PyCharm
# @Time    : 2023/10/26 21:21


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

# lxml: 第三方解析器, pip install lxml
soup = BeautifulSoup(html, 'lxml')
# prettify: 用于美化html代码
print(soup.prettify())
