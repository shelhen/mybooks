# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.cookie数据处理.py
# @Software: PyCharm
# @Time    : 2023/11/19 20:56


from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.baidu.com')

cookie_list = browser.get_cookies()
cookie_dict = {x['name']: x['value'] for x in cookie_list}
print(cookie_dict)


# cookie设置
# browser.add_cookie({'name': '安娜'})

# cookie删除
# browser.delete_cookie('cookie_name')
# browser.delete_all_cookies()  # 删除全部
