# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午9:16
# @Author  : 顾安
# @File    : 6.ssl证书错误.py
# @Software: PyCharm

import requests


url = "https://chinasoftinc.com/owa"
# verify: 忽略证书错误
response = requests.get(url, verify=False)
print(response)

"""
requests.exceptions.SSLError
    当前报错可能有三种原因:
        1.网站证书过期
        2.url链接编写错误
        3.python环境出现问题
            3.1.检查当前环境中的urllib3的版本
                macOS系统中的urllib3版本控制在1.26
                windows系统中的urllib3版本控制在1.25
        pip install urllib3==版本号会覆盖原有版本
"""

