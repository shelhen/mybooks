"""
https协议与http协议都是同一种网络协议
    https多了ssl加密层

http/https基于tcp实现的

tcp也是一种网络协议，python可以直接构造出来
"""

# python自带的一个包
import socket


tcp_server = socket.socket()
