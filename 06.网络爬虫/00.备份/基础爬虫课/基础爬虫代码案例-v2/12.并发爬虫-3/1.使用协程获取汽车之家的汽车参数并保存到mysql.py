# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.使用协程获取汽车之家的汽车参数并保存到mysql.py
# @Software: PyCharm
# @Time    : 2023/11/9 21:02

"""
分析思路:
    1.在首页中获取汽车id
    2.将获取到的汽车id拼接到api数据接口中
    3.保存数据
"""
import redis
import chardet
import hashlib
import asyncio
import aiohttp
import aiomysql
from lxml import etree


class CarSpider:
    redis_client = redis.Redis()

    def __init__(self):
        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exf4x0/?pvareaid=102179#currengpostion'
        self.api_url = 'https://cacheapigo.che168.com/CarProduct/GetParam.ashx?specid={}'
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

    # 获取汽车id
    async def get_car_id(self, page, session, pool):
        async with session.get(self.url.format(page), headers=self.headers) as response:
            content = await response.read()
            encoding = chardet.detect(content)['encoding']  # 汽车之家会检测是否频繁请求, 如果频繁请求则将页面替换成UTF8编码格式并无法获取汽车id
            # print(encoding)
            if encoding == 'GB2312' or encoding == 'ISO-8859-1':
                result = content.decode('gbk')
            else:
                result = content.decode(encoding)
                print('被反爬了...')

            tree = etree.HTML(result)
            id_list = tree.xpath('//ul[@class="viewlist_ul"]/li/@specid')
            if id_list:
                print(id_list)
                tasks = [asyncio.create_task(self.get_car_info(spec_id, session, pool)) for spec_id in id_list]
                await asyncio.wait(tasks)

    # 当获取到页面中所有的汽车id之后要进行api连接的拼接并获取api数据
    async def get_car_info(self, spec_id, session, pool):
        tasks = list()
        async with session.get(self.api_url.format(spec_id), headers=self.headers) as response:
            result = await response.json()
            if result['result'].get('paramtypeitems'):
                item = dict()
                item['name'] = result['result']['paramtypeitems'][0]['paramitems'][0]['value']
                item['price'] = result['result']['paramtypeitems'][0]['paramitems'][1]['value']
                item['brand'] = result['result']['paramtypeitems'][0]['paramitems'][2]['value']
                item['altitude'] = result['result']['paramtypeitems'][1]['paramitems'][2]['value']
                item['breadth'] = result['result']['paramtypeitems'][1]['paramitems'][1]['value']
                item['length'] = result['result']['paramtypeitems'][1]['paramitems'][0]['value']
                tasks.append(asyncio.create_task(self.save_car_info(item, pool)))
            else:
                print('数据不存在...')

    @staticmethod
    def get_md5(dict_item):
        md5 = hashlib.md5()
        md5.update(str(dict_item).encode('utf-8'))
        return md5.hexdigest()

    async def save_car_info(self, item, pool):
        # 使用异步上下文管理器创建链接对象以及游标对象
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                val_md5 = self.get_md5(item)
                # 保存成功返回1, 保存失败返回0
                redis_result = self.redis_client.sadd('car:filter', val_md5)
                if redis_result:
                    sql = """
                        insert into car_info(
                            id, name, price, brand, altitude, breadth, length) values (
                                %s, %s, %s, %s, %s, %s, %s
                            );
                    """
                    try:
                        await cursor.execute(sql, (0,
                                                   item['name'],
                                                   item['price'],
                                                   item['brand'],
                                                   item['altitude'],
                                                   item['breadth'],
                                                   item['length']
                                                   ))
                        await conn.commit()
                        print('插入成功...')
                    except Exception as e:
                        print('数据插入失败:', e)
                        await conn.rollback()
                else:
                    print('数据重复...')

    # 启动函数
    async def main(self):
        # 创建数据库连接池并获取游标对象
        async with aiomysql.create_pool(user='root', password='root', db='py_spider') as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    # 创建表
                    create_table_sql = """
                        create table car_info(
                            id int primary key auto_increment,
                            name varchar(100),
                            price varchar(100),
                            brand varchar(100),
                            altitude varchar(100),
                            breadth varchar(100),
                            length varchar(100)
                        );
                    """

                    # 在异步代码中必须先要检查表是否存在, 直接使用if not语句无效
                    check_table_query = "show tables like 'car_info'"
                    result = await cursor.execute(check_table_query)  # 如果表存在返回1 不存在返回0
                    if not result:
                        await cursor.execute(create_table_sql)

            # 创建请求对象
            async with aiohttp.ClientSession() as session:
                tasks = [asyncio.create_task(self.get_car_id(page, session, pool)) for page in range(1, 16)]
                await asyncio.wait(tasks)


if __name__ == '__main__':
    car = CarSpider()
    asyncio.run(car.main())
