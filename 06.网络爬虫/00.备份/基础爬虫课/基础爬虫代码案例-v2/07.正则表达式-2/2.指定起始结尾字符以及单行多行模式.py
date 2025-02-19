# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.指定起始结尾字符以及单行多行模式.py
# @Software: PyCharm
# @Time    : 2023/10/31 20:15


import re

content = """001-苹果价格-60
002-橙子价格-70
003-香蕉价格-80
"""

# re.M: 允许换行匹配
for temp in re.findall(r'^\d+', content, re.M):
    print(temp)

for temp in re.findall(r'\d+$', content, re.M):
    print(temp)

"""
^: 以指定字符开头
$: 以指定字符结尾

re.M: 多行匹配模式, re正则默认是单行匹配
"""
