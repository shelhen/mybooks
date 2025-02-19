"""
爬虫的通用执行流程
    1.定义请求连接 一般会用列表进行临时存储
    2.对列表进行遍历
    3.依次拿到url连接之后对连接发送网络请求
    4.获取到网站服务器的数据并进行数据清洗
    5.数据入库
"""


url_list = ['https://www.baidu.com', 'https://www.google.com']

for url in url_list:
    # 在for循环中获取元素url并发送请求
    # 获取到响应数据并进行数据清洗
    # 保存数据
    pass
