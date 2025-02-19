# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.页面等待.py
# @Software: PyCharm
# @Time    : 2023/11/19 21:12


"""
某些网站的控件是动态生成的, 在生成控件时需要消耗一定的时间
    需要进入到首页后等待一些动态控件加载完成
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
wait_ob = WebDriverWait(browser, 10)
time.sleep(10)

browser.get('https://www.jd.com')

search_input = wait_ob.until(EC.presence_of_element_located((By.ID, 'key')))
print(search_input)

# 可以使用WebElement对象进行交互操作
search_input.send_keys('口红')
time.sleep(2)

# 通过以上方式完成搜索点击
# 点击成功之后会跳转到登录页
