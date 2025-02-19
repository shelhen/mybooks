# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.获取单个节点.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:26


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://news.baidu.com/')

element_obj_1 = browser.find_element(By.ID, 'ww')
print(element_obj_1)

element_obj_2 = browser.find_element(By.CSS_SELECTOR, '#ww')
print(element_obj_2)

element_obj_3 = browser.find_element(By.CSS_SELECTOR, '.word')
print(element_obj_3)


element_obj_4 = browser.find_element(By.XPATH, '//*[@id="ww"]')
print(element_obj_4)
