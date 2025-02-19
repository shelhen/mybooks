# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.指定字符范围匹配.py
# @Software: PyCharm
# @Time    : 2023/10/31 20:12


import re

content = 'asdasfqweq1231@!#@~#@@#'

for temp in re.findall(r'[\d\W]', content):
    print(temp)

