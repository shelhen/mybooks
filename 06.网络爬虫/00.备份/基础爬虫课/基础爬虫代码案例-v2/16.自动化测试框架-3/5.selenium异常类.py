# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.selenium异常类.py
# @Software: PyCharm
# @Time    : 2023/11/21 20:44


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


browser = webdriver.Chrome()

try:
    browser.set_page_load_timeout(3)
    browser.get('https://www.google.com')
except TimeoutException as e:
    print('请求超时:', e)
    browser.close()


try:
    browser.find_element(By.ID, 'abcd')
except NoSuchElementException as e:
    print('元素标签未找到:', e)

