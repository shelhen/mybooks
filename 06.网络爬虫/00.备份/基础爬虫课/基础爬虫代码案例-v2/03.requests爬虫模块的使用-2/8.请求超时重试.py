# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午9:30
# @Author  : 顾安
# @File    : 8.请求超时重试.py
# @Software: PyCharm


import time
from retrying import retry

num = 1


# 主要作用是设置一个模块的最大重试次数而已
@retry(stop_max_attempt_number=3)
def test():
    global num
    print(f'num={num}')
    num += 1
    time.sleep(1)
    for i in 100:
        print('i', i)


if __name__ == '__main__':
    try:
        test()
    except Exception as e:
        print('程序异常:', e)
    else:
        print('没有异常')
