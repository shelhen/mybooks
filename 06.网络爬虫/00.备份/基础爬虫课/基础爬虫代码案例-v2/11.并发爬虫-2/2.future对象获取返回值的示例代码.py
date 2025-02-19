# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.future对象获取返回值的示例代码.py
# @Software: PyCharm
# @Time    : 2023/11/9 20:51


import asyncio


async def work():
    print(1)
    await asyncio.sleep(1)
    print(2)
    return 123


async def main():
    res = await asyncio.ensure_future(work())
    print(res)


asyncio.run(main())

"""
task任务与future任务必须使用await关键字调度运行才行
"""
