# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.正则-通配符.py
# @Software: PyCharm
# @Time    : 2023/10/29 21:23


"""
. 在正则是通配符
    但是不能匹配换行符 \n
"""


import re

content = """
苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的
"""

# print(re.findall(r'.色', content))  # 当前findall方法返回的数据类型是一个列表

for result in re.findall(r'.色', content):
    print(result)
