# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.提取标签内容以及标签属性值.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:47


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.douban.com')

result_1 = browser.find_element(By.TAG_NAME, 'h1')
print(result_1.text)


result_2 = browser.find_element(By.LINK_TEXT, '下载豆瓣 App')
print(result_2.get_attribute('href'))

