# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.字符串切割.py
# @Software: PyCharm
# @Time    : 2023/10/31 20:49

import re

names = '关羽; 张飞, 赵云,   马超, 黄忠  李逵'


name_list = re.split(r'[;,\s]\s*', names)
print(name_list)
