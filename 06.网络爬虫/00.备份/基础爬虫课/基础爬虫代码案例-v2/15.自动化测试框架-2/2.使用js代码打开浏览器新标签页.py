# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.使用js代码打开浏览器新标签页.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:07


import time
from selenium import webdriver


browser = webdriver.Chrome()

browser.get('http://www.taobao.com')
time.sleep(3)

js = 'window.open("http://www.jd.com")'
browser.execute_script(js)
time.sleep(3)
