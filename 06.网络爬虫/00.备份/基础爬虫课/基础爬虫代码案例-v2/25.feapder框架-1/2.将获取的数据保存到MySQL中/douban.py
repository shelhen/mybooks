# -*- coding: utf-8 -*-
"""
Created on 2023-12-19 21:04:59
---------
@summary:
---------
@author: poppies
"""

import feapder
from douban_feapder_item import DoubanFeapderItem


class Douban(feapder.AirSpider):
    def start_requests(self):
        for page in range(10):
            yield feapder.Request(f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, request, response):
        li_list = response.xpath('//ol/li/div[@class="item"]')
        for li in li_list:
            item = DoubanFeapderItem()
            item['title'] = li.xpath('./div[@class="info"]/div/a/span[1]/text()').extract_first()
            item['detail_url'] = li.xpath('./div[@class="info"]/div/a/@href').extract_first()
            item['score'] = li.xpath('.//div[@class="star"]/span[2]/text()').extract_first()
            yield feapder.Request(item['detail_url'], callback=self.detail_parse, item=item)

    def detail_parse(self, request, response):
        """
        :param request:
        :param response:
        :return:
        每一部电影详情页中的页面结构可能不一样, 需要判断详情数据对应的xpath规则是否存在
            如果存在则直接提取
            如果不存在则自定义新的xpath规则
        """
        if response.xpath('//div[@class="indent"]/span[@class="all hidden"]//text()'):
            request.item['detail_text'] = response.xpath(
                '//div[@class="indent"]/span[@class="all hidden"]//text()').extract_first().strip()
        else:
            request.item['detail_text'] = response.xpath(
                '//div[@class="indent"]/span[1]//text()').extract_first().strip()

        # 进行数据入库
        yield request.item


if __name__ == "__main__":
    Douban().start()
