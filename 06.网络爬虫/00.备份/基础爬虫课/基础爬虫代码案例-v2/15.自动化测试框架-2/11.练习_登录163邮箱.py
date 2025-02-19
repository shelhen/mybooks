# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.练习:登录163邮箱.py
# @Software: PyCharm
# @Time    : 2023/11/19 21:47


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class WyMail:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_email(self, url):
        self.driver.get(url)
        time.sleep(1)

    def login_email(self, email, password):
        iframe = self.driver.find_element(By.XPATH, '//div[@id="loginDiv"]/iframe[@scrolling = "no"]')

        # 登录表单为一个子页面, 需要切入到当前这个子页面中
        self.driver.switch_to.frame(iframe)

        self.driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//div[@class="u-input box"]//input[@name="password"]').send_keys(password)

        self.driver.find_element(By.XPATH, './/*[@id="dologin"]').click()

    def close(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == '__main__':
    email = WyMail()
    email.open_email('https://mail.163.com/')
    email.login_email('wt_poppies@163.com', 'wt199486')
    email.close()
