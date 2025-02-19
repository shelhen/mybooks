# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.正则-匹配任意次数(包含0次).py
# @Software: PyCharm
# @Time    : 2023/10/29 21:30


import re


content = """
苹果，是绿色的
橙子，是橙色的
香蕉，是黄色的
乌鸦，是黑色的
猴子，
"""

for temp in re.findall(r'，.*', content):
    print(temp)
