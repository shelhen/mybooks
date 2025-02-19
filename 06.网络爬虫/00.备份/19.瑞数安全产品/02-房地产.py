

import requests
from lxml import etree
import execjs


url = 'http://www.fangdi.com.cn/index.html'

headers = {
    'Host': 'www.fangdi.com.cn',
    'Referer': 'http://www.fangdi.com.cn/service/service_law_detail_img2.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


# 几次请求  2
requests = requests.session()  # 携带响应的cookie


def first_request():
    response = requests.get(url, headers=headers)
    print(response)
    obj_html = etree.HTML(response.text)
    content_data = obj_html.xpath('//meta[2]/@content')[0]
    func_code = obj_html.xpath('//script[2]/text()')[0]
    return content_data, func_code


def two_request(content_data, func_code):
    with open('01-房地产.js', encoding='utf-8')as f:
        js_code = f.read().replace('"conten_code"', content_data).replace("'func_code'", func_code)

    js = execjs.compile(js_code)
    cookie = js.call('get_cookie')
    cookies = {
        'FSSBBIl1UgzbN7N80T': cookie.split(';')[0].split('=')[1]
    }
    print(cookies)
    res = requests.get(url, headers=headers, cookies=cookies)
    print(res.status_code)
    res.encoding = 'utf-8'
    print(res.text)

content_data, func_code = first_request()
two_request(content_data, func_code)












