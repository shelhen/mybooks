# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.使用jsonpath进行数据提取.py
# @Software: PyCharm
# @Time    : 2023/10/26 20:10

import jsonpath

info = {
    "error_code": 0,
    "stu_info": [
        {
            "id": 2059,
            "name": "小白",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道xx号",
            "grade": "天蝎座",
            "phone": "1837830xxxx",
            "gold": 10896,
            "info": {
                "card": 12345678,
                "bank_name": '中国银行'
            }
        },
        {
            "id": 2067,
            "name": "小黑",
            "sex": "男",
            "age": 28,
            "addr": "河南省济源市北海大道xx号",
            "grade": "天蝎座",
            "phone": "87654321",
            "gold": 100
        }
    ]
}


# 获取列表中第一个字典中的name值
# result_1 = info['stu_info'][0]['name']
# print(result_1)
# result_2 = info['stu_info'][1]['name']
# print(result_2)

# 使用jsonpath取值
# pip install jsonpath
"""
jsonpath方法需要接收两个参数
    你要提取的字典对象
    提取规则
"""
result_1 = jsonpath.jsonpath(info, '$.stu_info[0].name')  # 返回的是一个列表对象
print(result_1)
result_2 = jsonpath.jsonpath(info, '$.stu_info[1].name')
print(result_2)

# 使用模糊匹配的方式快速定位我想要的值
result_3 = jsonpath.jsonpath(info, '$..name')
print(result_3)


result_4 = jsonpath.jsonpath(info, '$..bank_name')
print(result_4)







