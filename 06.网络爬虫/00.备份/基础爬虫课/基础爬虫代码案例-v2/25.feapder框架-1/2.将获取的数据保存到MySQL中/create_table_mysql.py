# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : create_table_mysql.py
# @Software: PyCharm
# @Time    : 2023/12/19 21:09


from feapder.db.mysqldb import MysqlDB

# 在feapder框架连接mysql时, 只需要创建连接对象, 无需创建游标
db = MysqlDB(ip='localhost', port=3306, user_name='root', user_pass='root', db='py_spider')

create_table = """
    create table if not exists douban_feapder(
        id int primary key auto_increment,
        title varchar(255) not null,
        score varchar(10) not null,
        detail_url varchar(255) not null,
        detail_text text
    );
"""

db.execute(create_table)


# 数据插入测试
# insert_sql = """
#     insert into douban_feapder values (0, '测试数据', 10, 'https://www.baidu.com', '详情测试数据');
# """
# db.add(insert_sql)
