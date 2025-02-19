# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 下午8:56
# @Author  : 顾安
# @File    : 1.python中的编解码.py
# @Software: PyCharm


str_code = 'abc'

byte_code = str_code.encode('utf-8')
print(type(byte_code))

print(type(byte_code.decode('utf-8')))


"""
在之后进行页面数据抓取的过程中, 建议先看当前页面中的编码集
    如果页面返回的数据打印出来时乱码, 那么首先要排查的是页面的编码集
"""
