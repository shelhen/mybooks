from lxml import etree
import re
import requests
import execjs

class State_Grid:
    def __init__(self):
        self.url = ('http://www.sgcc.com.cn/html/sgcc/'
                    'col2022121225/column_2022121225_2.shtml')
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        self.session = requests.session()

    def first_requset(self):
        first_response = self.session.get(url=self.url,headers=self.headers)
        html = etree.HTML(first_response.text)
        ts_cd = html.xpath('//script[@r="m"]/text()')[0]
        content = re.findall('ta content="(.*?)" r="m',first_response.text,re.S)[0]
        with open('./teest.js', 'r', encoding='UTF-8') as file:
            file = file.read().replace("arg1_content",content).replace("'arg2_function'",ts_cd)
        ctll = execjs.compile(file)
        cookie = ctll.call('go')
        all_cookie = re.findall('(.*?); path=/;',cookie,re.S)[0]
        list_cookie = all_cookie.split('=')
        print(list_cookie)
        cookie = {
            "FSSBBIl1UgzbN7NS":first_response.cookies.get("FSSBBIl1UgzbN7NS"),
            list_cookie[0]:list_cookie[1]
        }
        return cookie

    def second_requset(self):
        cookies = self.first_requset()
        print(cookies)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://www.sgcc.com.cn/html/sgcc/col2022121225/column_2022121225_2.shtml",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        response = self.session.get(url=self.url,cookies=cookies,headers=headers)
        print(response)


if __name__ == '__main__':
    state_grid = State_Grid()
    state_grid.second_requset()
