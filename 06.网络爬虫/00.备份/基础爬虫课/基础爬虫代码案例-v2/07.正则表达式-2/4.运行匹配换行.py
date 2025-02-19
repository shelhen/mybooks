# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.运行匹配换行.py
# @Software: PyCharm
# @Time    : 2023/10/31 20:44

import re

html_object = """<div class="el">
        <p class="t1">           
            <span>
                <a>Python开发工程师</a>
            </span>
        </p>
        <span class="t2">南京</span>
        <span class="t3">1.5-2万/月</span>
</div>
<div class="el">
        <p class="t1">
            <span>
                <a>java开发工程师</a>
            </span>
		</p>
        <span class="t2">苏州</span>
        <span class="t3">1.5-2/月</span>
</div>
"""

for temp in re.findall(r'class=\"t1\">.*?<a>(.*?)</a>', html_object, re.DOTALL):
    print(temp)


"""
DOTALL: 让.可以匹配\n
"""


