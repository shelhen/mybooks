# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.py
# @Software: PyCharm
# @Time    : 2023/11/7 22:03

import aiohttp
import asyncio


url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}


async def get_baidu():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            result = await response.text()
        print(result)


if __name__ == "__main__":
    asyncio.run(get_baidu())
