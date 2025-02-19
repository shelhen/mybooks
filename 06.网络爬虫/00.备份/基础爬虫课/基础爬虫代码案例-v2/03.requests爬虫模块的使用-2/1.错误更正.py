# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午8:04
# @Author  : 顾安
# @File    : 1.错误更正.py
# @Software: PyCharm


import requests


"""
百川老师有所有的浏览器插件
    下课之后找百川老师获取离线插件包
"""

headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',

    'Cookie':
        'bid=4lm4eFeexRw; _pk_id.100001.4cf6=87c06bcd14df05ac.1696688065.; dbcl2="203083309:6nxgbP7jL+g"; __utmz=30149280.1697202759.7.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1697202759.7.2.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; _ga=GA1.1.813452036.1697717763; _ga_Y4GN1R87RG=GS1.1.1697717762.1.1.1697719508.0.0.0; ck=uiHF; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1697976317%2C%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.175456593.1696688066.1697787932.1697976317.10; __utmb=30149280.0.10.1697976317; __utmc=30149280; __utma=223695111.1001237010.1696688066.1697787932.1697976317.10; __utmb=223695111.0.10.1697976317; __utmc=223695111'
}

url = 'https://movie.douban.com/top250?start=0&filter='

response = requests.get(url, headers=headers)

# 获取请求头使用以下这种方式
print(response.request.headers.get('Cookie'))
# print(response.request.cookies)


"""
当前课件已更新, 更新后的课件找班班老师领取: 双双老师
"""


