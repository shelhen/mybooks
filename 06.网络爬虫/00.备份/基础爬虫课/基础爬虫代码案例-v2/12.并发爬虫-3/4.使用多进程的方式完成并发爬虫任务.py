# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.使用多进程的方式完成并发爬虫任务.py
# @Software: PyCharm
# @Time    : 2023/11/11 21:32


# from multiprocessing import Process
#
#
# p = Process(target='', args=(,))
#
# p.daemon = True


"""
守护线程和守护进程有什么用？
    防止子进程/子线程因为任务无法退出造成整个程序卡死
    
主进程/主线程如果代码走到最后一行, 即将准备退出的时候发现子线程/子进程任务没有完成
    全部退出 不管任务是否完成
"""
