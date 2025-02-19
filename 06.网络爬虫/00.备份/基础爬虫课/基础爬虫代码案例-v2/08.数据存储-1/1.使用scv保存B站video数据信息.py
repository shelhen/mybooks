# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.使用scv保存B站video数据信息.py
# @Software: PyCharm
# @Time    : 2023/11/2 20:09

import csv
import requests


class SaveVideoInfo:
    def __init__(self):
        self.url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?category_id=&search_type=video&ad_resource=5654&__refresh__=true&_extra=&context=&page={}&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E7%BE%8E%E5%A5%B3&qv_id=FQIEGMzTV3ib2rghYba6JlIVC7AVHcsS&source_tag=3&gaia_vtoken=&dynamic_offset=36&web_location=1430654&w_rid=c558b9c1dbd45b6070a654b9f597ab55&wts=1698926645'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Cookie': "buvid3=24B2D828-680C-AC77-E787-13669953D2F063538infoc; b_nut=1697620963; i-wanna-go-back=-1; b_ut=7; _uuid=3FCB9672-AD35-B791-34EB-FBB394C1055DF61815infoc; enable_web_push=DISABLE; home_feed_column=5; buvid4=C4202519-7247-E9C8-E20C-E27302EDE53564679-023101817-STZcpyLLRzNibWQwQhkmXw%3D%3D; buvid_fp=77df88e74294ee94582ad08cb5f71cf4; CURRENT_FNVAL=4048; rpdid=|(kmJY|k~u~u0J'uYm~Yk|m)k; header_theme_version=CLOSE; SESSDATA=486a3b8a%2C1713507656%2C2602c%2Aa1CjADLWhb8hOljLOeLuedVVT6dmPfFDlTTryt7ZuXcTQacp6C-HeRFrNK59oZVhcUxtISVkRFWXNpNDhLbzZUUVNyT0xpNS1TaFJCYUx0NWQzNm4taDhva3hjM1EzTmZpc3Myc2gtdHZNTkNEYTFrdzZqSWxFcURoSjY1djZpVEN2V3JwaEFjdnBBIIEC; bili_jct=996967c0ccbec984e13ab8ccbfcf01cc; DedeUserID=508205460; DedeUserID__ckMd5=73fc57c2f075cc42; browser_resolution=1920-853; CURRENT_QUALITY=120; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTkxNjUzOTEsImlhdCI6MTY5ODkwNjEzMSwicGx0IjotMX0.NFeZiUClRc6JlUBJR0GFIPUKH4nY3fBqDZbOPGGsLgU; bili_ticket_expires=1699165331; PVID=2; b_lsid=AF6BBEDD_18B8FE8EF6D; sid=dqkrmy6a"
        }

    def save(self):
        with open('video_info.csv', 'a', encoding='utf-8', newline='') as f:
            # 1.定义表头
            field_names = ['author', 'arcurl', 'tag']
            f_csv = csv.DictWriter(f, fieldnames=field_names)
            f_csv.writeheader()
            for page in range(1, 6):
                response = requests.get(self.url.format(page), headers=self.headers).json()
                for result in response['data']['result']:
                    item = dict()
                    item['author'] = result['author']
                    item['arcurl'] = result['arcurl']
                    item['tag'] = result['tag']
                    print(item)
                    f_csv.writerow(item)


svi = SaveVideoInfo()
svi.save()
