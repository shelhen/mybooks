# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.标签页操作.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:02


import time
from selenium import webdriver

# 创建浏览器对象
browser = webdriver.Chrome()

browser.get('http://www.baidu.com')
time.sleep(3)

# 在原有的标签页中重新访问一个新的网址
browser.get('http://www.jd.com')
time.sleep(3)


browser.close()
