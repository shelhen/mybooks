# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.协程函数的运行问题.py
# @Software: PyCharm
# @Time    : 2023/11/7 21:29


import asyncio


async def work():
    print(1)
    await asyncio.sleep(1)
    print(2)


async def main():
    await work()  # 协程函数必须使用await进行调度

asyncio.run(main())
