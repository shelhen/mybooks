# -*- coding: utf-8 -*-
# @Time    : 2023/10/22 下午8:30
# @Author  : 顾安
# @File    : 3.百度翻译.py
# @Software: PyCharm


import requests

url = 'https://fanyi.baidu.com/basetrans'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 '
                  '(KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'Cookie': 'APPGUIDE_10_6_5=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; '
              'SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=79ED59B3DF405E7BE0B2F089BF5636C0;'
              ' PSTM=1697716565; BAIDUID=79ED59B3DF405E7B87EFE83B3F670F21:FG=1;'
              ' BAIDUID_BFESS=79ED59B3DF405E7B87EFE83B3F670F21:FG=1; '
              'ZFY=E8UL64u1CWxtvnkjGKUmcr39lCirPsWnNcY4Ojzc6Ts:C; '
              'APPGUIDE_10_6_6=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1696754387,1697974256,1697977852;'
              ' Hm_lvt_afd111fa62852d1f37001d1f980b6800=1697974326,1697978022; '
              'Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1697978022; '
              'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1697978022; '
              'ab_sr=1.0.1_N2NjNDE3YzRiM2YzN2Q1MTliNWYyZWIwN2IxODE5NzMyYWMzMDM5OWU1MTlkM'
              'jg5MTU2MWIyZDc4Mjg0ZTRkYThjNTYwOWJjYzA0NTM5NDlkZjdiZjU4OTEzNDBjMmVhN2QwNDU'
              '3YjhkODA0NDViMmM1OTdiYjQ5ZDAzOWRkNWY5OTIwYjBmMmFjYWExOWZjMjQzYjBhOThkYzcyNzc5Mw=='
}

post_data = {
    'query': 'happy',
    'from': 'en',
    'to': 'zh',
    'token': '1ea8641117740bb5d46b93fad9a8ef33',
    'sign': '221212.492333'
}

response = requests.post(url, headers=headers, data=post_data).json()
print(response['trans'][0]['dst'])

"""
当前代码示例中的cookie需要大家自己在浏览器中获取
"""

