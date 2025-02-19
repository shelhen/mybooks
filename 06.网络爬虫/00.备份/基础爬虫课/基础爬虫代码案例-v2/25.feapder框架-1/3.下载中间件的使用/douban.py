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
    # def download_midware(self, request):
    #     request.headers = {
    #         'User-Agent': 'abc'
    #     }
    #
    #     request.proxies = {
    #         'http': 'http://127.0.0.1:7890'
    #     }
    #
    #     return request

    def custom_download_midware_1(self, request):
        request.headers = {
            'User-Agent': '123'
        }
        return request

    def custom_download_midware_2(self, request):
        request.cookies = {'a': 'b'}
        return request

    def start_requests(self):
        # request对象支持载入多个自定义中间件, 将download_midware的参数设置为一个列表即可
        # 但是一般不使用, 在一个中间件中配置好所有的request参数即可
        yield feapder.Request("https://movie.douban.com/top250?start=0&filter=", download_midware=[self.custom_download_midware_1, self.custom_download_midware_2])

    def parse(self, request, response):
        pass


if __name__ == "__main__":
    Douban().start()
