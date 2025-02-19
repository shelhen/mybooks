import requests
from lxml import etree
import execjs

def one():
    response = session.get(url, headers=headers)
    obj = etree.HTML(response.text) # type: ignore
    ts_code = obj.xpath('//script[1]/text()')[0]
    content_code =  obj.xpath('//meta[2]/@content')[0]
    func_src = 'https://www.nmpa.gov.cn' + obj.xpath('//script[2]/@src')[0]
    func_code = requests.get(func_src,headers=headers).text
    two(func_code,content_code,ts_code)


def two(func_code,content_code,ts_code):
    with open('药监局.js',encoding='utf-8') as f:
        code = f.read().replace('func_code',func_code).replace('content_code',content_code).replace('ts_code',ts_code)
    res = execjs.compile(code).call('main').split(';')[0].split('=')
    session.cookies[res[0]]=res[1]
    headers['Referer']=url
    response = session.get(url,headers=headers)
    response.encoding=response.apparent_encoding
    print(response)
    # print(response.text)


if __name__ == '__main__':
    url = 'https://www.nmpa.gov.cn/datasearch/home-index.html'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    session=requests.session()
    one()
