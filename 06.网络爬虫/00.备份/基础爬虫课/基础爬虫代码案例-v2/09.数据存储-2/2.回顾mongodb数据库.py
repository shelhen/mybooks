# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.回顾mongodb数据库.py
# @Software: PyCharm
# @Time    : 2023/11/5 21:14

# pip install pymongo
import pymongo

mongo_client = pymongo.MongoClient(host='localhost', port=27017)
collection = mongo_client['students']['stu_info']

# 插入单条数据
# student = {'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
# result = collection.insert_one(student)
# print(result)


# 插入多条数据
student_1 = {'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
student_2 = {'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}
result = collection.insert_many([student_1, student_2])
print(result)
