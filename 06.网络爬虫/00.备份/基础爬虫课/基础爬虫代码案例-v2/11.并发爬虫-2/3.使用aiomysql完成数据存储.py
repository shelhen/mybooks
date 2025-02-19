# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.使用aiomysql完成数据存储.py
# @Software: PyCharm
# @Time    : 2023/11/9 20:24


import asyncio
import aiomysql


async def conn_mysql():
    # 异步上下文管理器
    async with aiomysql.connect(host='localhost', port=3306, user='root', password='root', db='py_spider') as conn:
        async with conn.cursor() as cursor:
            await cursor.execute('select * from ali_work;')
            result = await cursor.fetchall()  # 如果不加await返回的是一个Future对象
            print(result)


asyncio.run(conn_mysql())

