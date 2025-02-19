# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.正则-贪婪模式与非贪婪模式.py
# @Software: PyCharm
# @Time    : 2023/10/29 21:44


import re

source = '<html><head><title>Title</title>'

for temp in re.findall(r'<.*>', source):
    print(temp)


"""
贪婪模式是尽可能多的去匹配符合规则的字符

非贪婪模式是尽可能少的去匹配符合规则的字符
"""

for temp in re.findall(r'<.*?>', source):
    print(temp)
