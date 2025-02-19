# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.页面的前进和后退.py
# @Software: PyCharm
# @Time    : 2023/11/19 21:41


import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.jd.com')
time.sleep(2)

browser.get('https://www.baidu.com')
time.sleep(2)


browser.back()  # 在同一个标签页中进行后退
time.sleep(1)

browser.forward()
time.sleep(1)
