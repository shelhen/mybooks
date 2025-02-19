# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.使用aiohttp完成并发爬虫任务.py
# @Software: PyCharm
# @Time    : 2023/11/9 20:03


import asyncio
import aiohttp
from aiohttp import ClientResponse
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250?start={}&filter='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}


async def get_movie_info(page):
    # aiohttp请求对象与响应对象都是通过上下文管理器创建的
    async with aiohttp.ClientSession() as session:  # 上下文管理器创建请求对象
        async with session.get(url.format(page * 25), headers=headers) as response:  # 请求完成后返回的响应对象
            soup = BeautifulSoup(await response.text(), 'lxml')
            div_list = soup.find_all('div', class_='hd')
            for title in div_list:
                print(title.get_text())


# async def main():
#     tasks = [asyncio.create_task(get_movie_info(page)) for page in range(10)]
#     await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(get_movie_info(page)) for page in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))

    # asyncio.run(main())


"""
上下文管理器是用来开启与关闭对象的
    IO对象: 文件读写对象、网络请求对象、文件读写对象    
    使用完IO对象之后要释放, 提高系统性能

    session请求对象是一种IO对象, 使用完请求对象之后需要释放
    session.close()
    
    同理: 执行完请求对象后返回的响应对象response也是一种IO对象
        需要关闭
    response.close()
"""