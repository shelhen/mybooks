# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.正则分组.py
# @Software: PyCharm
# @Time    : 2023/10/31 20:26

import re

content = """苹果，苹果是绿色的
橙子，橙子是橙色的
香蕉，香蕉是黄色的
"""


for temp in re.findall(r'(.*)，', content, re.M):
    print(temp)


"""
在正则表达式中想要取到部分数据可以使用小括号进行分组获取
"""


person_info = """张三，手机号码15945678901
李四，手机号码13945677701
王二，手机号码13845666901
"""


for temp in re.findall(r'^(.+)，.*?(\d{11})', person_info, re.M):
    print(temp)


# 给不同的分组取别名
for temp in re.finditer(r'^(?P<user_name>.+)，.*?(?P<mobile>\d{11})', person_info, re.M):
    print(temp.group('user_name'), temp.group('mobile'))
