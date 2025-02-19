# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.查询请求信息.py
# @Software: PyCharm
# @Time    : 2023/11/16 21:56


import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.baidu.com')

# 获取访问的页面源代码
# html = browser.page_source
# print(type(html))

# 获取cookie
print(browser.get_cookies())


# 获取请求的url地址
browser.get('https://www.360buy.com')
print(browser.current_url)  # 获取的是浏览器最终访问的页面
