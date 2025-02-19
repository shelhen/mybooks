# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.退出浏览器.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:17


import time
from selenium import webdriver


browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
time.sleep(3)

# 如果当前只剩下一个标签页则会退出浏览器
browser.close()

browser.quit()  # 让浏览器退出
