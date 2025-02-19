# -*- coding: utf-8 -*-
"""
Created on 2023-12-19 21:48:42
---------
@summary:
---------
@author: poppies
"""

import feapder


class Douban(feapder.AirSpider):
    def download_midware(self, request):
        request.proxies = {
            'http': 'http://127.0.0.1:8080'
        }

    def start_requests(self):
        # request对象支持载入多个自定义中间件, 将download_midware的参数设置为一个列表即可
        # 但是一般不使用, 在一个中间件中配置好所有的request参数即可
        yield feapder.Request("https://movie.douban.com/top250?start=0&filter=")

    def validate(self, request, response):
        # print('响应状态码:', response.status_code)
        if response.status_code != 200:
            print('响应状态码异常:', response.status_code)
            # return False  # 抛弃当前请求
            raise Exception('请求重试')

    def parse(self, request, response):
        pass


if __name__ == "__main__":
    Douban().start()
