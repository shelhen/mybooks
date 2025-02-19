# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.页面定位与操作.py
# @Software: PyCharm
# @Time    : 2023/11/16 21:40


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 创建浏览器对象
browser = webdriver.Chrome()

# 访问百度首页
browser.get('http://www.baidu.com')

# 定位指定元素 - 输入框
browser.find_element(By.ID, 'kw').send_keys('java')
time.sleep(3)

# 定位指定元素 - 按钮
browser.find_element(By.ID, 'su').click()

time.sleep(5)
