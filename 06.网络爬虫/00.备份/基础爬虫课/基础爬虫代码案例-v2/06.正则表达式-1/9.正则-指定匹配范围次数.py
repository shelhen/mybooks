# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.正则-指定匹配范围次数.py
# @Software: PyCharm
# @Time    : 2023/10/29 21:40


import re


content = '红彤彤，绿油油，黑乎乎，绿油油油油'

for temp in re.findall(r'油{3,4}', content):
    print(temp)
