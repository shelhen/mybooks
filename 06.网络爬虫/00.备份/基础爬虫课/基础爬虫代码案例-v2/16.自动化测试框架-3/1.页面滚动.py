# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.页面滚动.py
# @Software: PyCharm
# @Time    : 2023/11/21 20:02


import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://36kr.com/')

for num in range(1, 10):
    # 绝对位置
    # browser.execute_script(f'window.scrollTo(0, {num * 700})')

    # 相对位置
    browser.execute_script(f'window.scrollBy(0, {num * 700})')
    time.sleep(1)

