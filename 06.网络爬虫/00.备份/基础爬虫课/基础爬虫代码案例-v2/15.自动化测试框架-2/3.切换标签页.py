# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.切换标签页.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:10


import time
from selenium import webdriver


browser = webdriver.Chrome()

browser.get('https://www.taobao.com')
time.sleep(3)

js = 'window.open("https://www.jd.com")'
browser.execute_script(js)
time.sleep(3)


# 切换到第一个标签页
browser.switch_to.window(browser.window_handles[0])
time.sleep(1)

# 切换到第二个标签页
browser.switch_to.window(browser.window_handles[1])
time.sleep(1)

# 关闭当前所在的标签页
browser.close()
time.sleep(2)

browser.switch_to.window(browser.window_handles[0])
browser.close()