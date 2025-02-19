# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.bs中的解析方法-find_all.py
# @Software: PyCharm
# @Time    : 2023/10/26 21:27


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

# 1.创建soup对象并指定页面代码解析器
soup = BeautifulSoup(html, "lxml")

# 2. 根据标签名称查询对应标签
# find_all: 查询符合条件的所有标签
# fand_all返回的是列表
res_1 = soup.find_all('a')
print(res_1)
res_2 = soup.find_all('p')
print(res_2)

# find_all方法支持传递一个列表
# 匹配在列表中传递的所有元素名的任意一个
res_3 = soup.find_all(['title', 'p'])
print(res_3)






