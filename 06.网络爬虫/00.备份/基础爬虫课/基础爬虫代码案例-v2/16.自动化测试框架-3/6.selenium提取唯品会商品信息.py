# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.selenium提取唯品会商品信息.py
# @Software: PyCharm
# @Time    : 2023/11/21 20:55


import time
from random import randint
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class WpShop:
    mongo_client = MongoClient()
    collection = mongo_client['py_spider']['wp_shop']

    # 创建浏览器配置对象
    options = webdriver.ChromeOptions()

    # 屏蔽图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option('prefs', prefs)

    # 创建浏览器对象
    browser = webdriver.Chrome(options=options)

    # 访问唯品会首页并等待载入输入框并输入关键字
    def index_html(self):
        self.browser.get('https://www.vip.com/')
        wait = WebDriverWait(self.browser, 10)

        el_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="J-search"]/div[1]/input')
        ))

        el_input.send_keys('电脑')

        el_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="J-search"]/div[1]/a')
        ))
        time.sleep(2)
        el_button.click()

        # 当成功进入到商品列表页之后等待1~3秒再进行后续操作
        time.sleep(randint(1, 3))

    # 点击完成后会进入到商品列表页, 让浏览器自动下滑加载商品列表数据
    def drop_down(self):
        for i in range(1, 13):
            js_code = f'window.scrollTo(0, {i * 1000})'
            self.browser.execute_script(js_code)
            time.sleep(randint(1, 3))

    # 数据提取
    def parse_data(self):
        self.drop_down()
        div_list = self.browser.find_elements(By.XPATH,
                                              '//section[@id="J_searchCatList"]/div[@class="c-goods-item  J-goods-item c-goods-item--auto-width"]')
        for div in div_list:
            price = div.find_element(By.XPATH, './/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]').text
            title = div.find_element(By.XPATH, './/div[2]/div[2]').text

            item = {
                'title': title,
                'price': price
            }
            print(item)
            self.save_data(item)
        self.next_page()

    # 翻页控制
    def next_page(self):
        try:
            next_button = self.browser.find_element(By.XPATH, '//*[@id="J_nextPage_link"]')
            if next_button:
                print(next_button.get_attribute('href'))
                next_button.click()
                self.parse_data()
            else:
                self.browser.close()
        except NoSuchElementException as e:
            print('最后一页:', e)
            self.browser.quit()

    # 数据保存
    def save_data(self, item):
        self.collection.insert_one(item)

    # 启动函数
    def main(self):
        self.index_html()
        self.parse_data()


if __name__ == '__main__':
    wp_shop = WpShop()
    wp_shop.main()
