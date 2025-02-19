# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.匹配中文.py
# @Software: PyCharm
# @Time    : 2023/10/31 20:56


import re

title = '你好，hello，世界, 123'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(title)

print(result)
