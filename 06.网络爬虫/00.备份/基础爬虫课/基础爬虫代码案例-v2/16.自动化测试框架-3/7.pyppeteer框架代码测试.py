# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.pyppeteer框架代码测试.py
# @Software: PyCharm
# @Time    : 2023/11/21 22:18


import asyncio
from lxml import etree
from pyppeteer import launch


async def get_movie():
    # headless=False: 开启浏览器界面
    # devtools:True: 开启浏览器开发工具
    # userDataDir: 数据持久化
    # args=['--disable-infobars']: 禁用提示条
    browser = await launch(headless=False, devtools=False, userDataDir='./userdata',
                           args=['--disable-blink-features=AutomationControlled'])
    page = await browser.newPage()

    # 隐藏WebDriver
    # await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    # 设置显示界面与浏览器窗口大小一致
    width, height = 1366, 768
    await page.setViewport({'width': width, 'height': height})

    for page_num in range(10):
        await page.goto(f'https://movie.douban.com/top250?start={page_num * 25}&filter=')
        await page.waitForXPath('//ol[@class="grid_view"]')  # 等待标签加载完毕
        tree = etree.HTML(await page.content())
        li_list = tree.xpath('//ol[@class="grid_view"]/li')
        for li in li_list:
            print(li.xpath('.//span[@class="title"]/text()')[0])

    await browser.close()


asyncio.get_event_loop().run_until_complete(get_movie())
