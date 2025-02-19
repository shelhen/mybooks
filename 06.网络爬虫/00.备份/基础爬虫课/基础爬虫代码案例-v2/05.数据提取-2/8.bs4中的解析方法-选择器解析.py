# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.bs4中的解析方法-选择器解析.py
# @Software: PyCharm
# @Time    : 2023/10/26 21:50

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


"""
标签选择器
"""
soup = BeautifulSoup(html, 'lxml')
# select使用的是前端的css选择器方法来进行标签定位, 和之前使用的find_all类似
# 标签名称选择器进行筛选
# 标签选择器返回的是一个列表
res_1 = soup.select('title')
print(res_1)
res_2 = soup.select('a')
print(res_2)

"""
类选择器
"""
res_3 = soup.select('.sister')
print(res_3)

"""
id选择器
    如果在页面中存在id属性, 建议优先使用id属性去匹配数据
    id属性不重复
"""
res_4 = soup.select('#link3')
print(res_4)

"""
层级选择器
"""
res_5 = soup.select('p #link1')
print(res_5)

"""
属性选择器
"""
res_6 = soup.select('a[href="http://example.com/elsie"]')
print(res_6)
res_7 = soup.select('p[class="title"]')
print(res_7)




