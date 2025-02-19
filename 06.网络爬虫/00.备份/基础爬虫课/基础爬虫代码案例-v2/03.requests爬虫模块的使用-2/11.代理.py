# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午9:51
# @Author  : 顾安
# @File    : 11.代理.py
# @Software: PyCharm


import requests

"""
如果想要获取一个超大型的电商网站中的数据，需要24小时不停的抓取数据
    可能造成你电脑的ip被封禁
"""

# proxies = {
#     # 可以使用自己定义的ip地址去访问目标网站, 从而达到隐藏自己本机真实ip的功能
#     'http': 'http://10.92.118.47:8080',
#     'https': 'https://10.92.118.47:3290'
# }
#
# response = requests.get('https://www.baidu.com', proxies=proxies, timeout=3)
# print(response)


# 使用免费代理进行请求测试
ip = '127.0.0.1'
port = 7890

proxies = {
    'http': f'http://{ip}:{port}',
    'https': f'https://{ip}:{port}'
}


headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}


url = 'http://httpbin.org/ip'

response = requests.get(url=url, headers=headers, proxies=proxies, timeout=4)
print(response.text)
