# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.绕过检测.py
# @Software: PyCharm
# @Time    : 2023/11/21 20:13

import time
from selenium import webdriver


# 创建浏览器信息配置对象
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(options=options)


browser.get('https://bot.sannysoft.com/')
time.sleep(10)
