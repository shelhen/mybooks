# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.浏览器配置.py
# @Software: PyCharm
# @Time    : 2023/11/21 20:20


import time
from selenium import webdriver

# 创建浏览器配置对象
options = webdriver.ChromeOptions()

# 禁止图片加载
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option('prefs', prefs)

# 设置UA
user_agent = 'abc'
options.add_argument(f'user-agent={user_agent}')

# 隐藏浏览器开发者警告
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 代理配置
options.add_argument("--proxy-server=http://127.0.0.1:7890")

browser = webdriver.Chrome(options=options)
browser.get('https://www.taobao.com')
time.sleep(30)
