# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.动作链.py
# @Software: PyCharm
# @Time    : 2023/11/21 20:33
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)

log = browser.find_element(By.XPATH, '//div[@id="iframewrapper"]/iframe')
browser.switch_to.frame(log)

source = browser.find_element(By.ID, 'draggable')
target = browser.find_element(By.ID, 'droppable')

actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()  # 执行动作链

time.sleep(3)
