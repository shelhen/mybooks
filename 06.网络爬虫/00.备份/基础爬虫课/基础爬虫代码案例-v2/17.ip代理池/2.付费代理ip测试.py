# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.付费代理ip测试.py
# @Software: PyCharm
# @Time    : 2023/11/26 20:46


import requests

# 提取代理API接口，获取1个代理IP
api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=oyhtwjy5v5vvu9dda8dc&num=10&signature=1l1yri642vuzkxzwki6nxzhotl0ypmc6&pt=1&format=json&sep=1"

# 获取API接口返回的代理IP
proxy_ip_list = requests.get(api_url).json()['data']['proxy_list']

# 白名单方式（需提前设置白名单）
for proxy_ip in proxy_ip_list:
    proxies = {
        "http": "http://%(proxy)s" % {"proxy": proxy_ip},
        # "https": "https://%(proxy)s" % {"proxy": proxy_ip}
    }

    print(proxies)
    # 要访问的目标网页
    target_url = "https://dev.kdlapi.com/testproxy"

    # 使用代理IP发送请求
    try:
        response = requests.get(target_url, proxies=proxies)
        if response.status_code == 200:
            print(response.text)
    except Exception as e:
        print('请求异常:', e)


