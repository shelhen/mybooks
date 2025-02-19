# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.获取多个节点.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:38


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://movie.douban.com/top250')


# 定位25个电影信息
# result = browser.find_elements(By.CSS_SELECTOR, '.item')
# print(result)

result = browser.find_elements(By.XPATH, '//div[@class="item"]')
print(result)


"""
find_element: 返回的是单个对象
find_elements: 返回的是一个列表
"""