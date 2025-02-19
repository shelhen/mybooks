# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.使用json模块保存4399游戏信息.py
# @Software: PyCharm
# @Time    : 2023/11/2 20:41

import json
import requests
from lxml import etree

url = 'https://www.4399.com/flash/'

response = requests.get(url).content.decode('gbk')
tree = etree.HTML(response)

a_list = tree.xpath("//ul[@class='n-game cf']/li/a")

game_info = list()

for a in a_list:
    item = dict()
    item['href'] = a.xpath('./@href')[0]
    item['title'] = a.xpath('./b/text()')[0]
    game_info.append(item)

with open('game_info.json', 'w', encoding='utf-8') as f:
    # f.write(json.dumps(game_info))
    f.write(json.dumps(game_info, indent=4, ensure_ascii=False))

