# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.jsonpath练习.py
# @Software: PyCharm
# @Time    : 2023/10/26 20:26


import jsonpath

info = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
             },
            {"category": "fiction",
             "author": "J. R. R. Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-395-19395-8",
             "price": 22.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}


# 1. 提取第一本书籍的title
result = jsonpath.jsonpath(info, '$.store.book[0].title')
print(result)
# 以下代码中的效果与以上代码一致
# result = jsonpath.jsonpath(info, '$.store.book[0][title]')
# print(result)

# 2. 提取2、3、4三本书的标题
result = jsonpath.jsonpath(info, '$.store.book[1,2,3].title')
print(result)
result = jsonpath.jsonpath(info, '$.store.book[1:4].title')
print(result)

# 3. 提取第一本和第三本书籍的名称
result = jsonpath.jsonpath(info, '$.store.book[::2].title')
print(result)
result = jsonpath.jsonpath(info, '$.store.book[0,2].title')
print(result)

# 4. 提取最后一本书籍的名称
result = jsonpath.jsonpath(info, '$.store.book[(@.length-1)].title')
print(result)
result = jsonpath.jsonpath(info, '$.store.book[-1:].title')
print(result)


# 5. 提取价格小于10的书籍标题
result = jsonpath.jsonpath(info, '$.store.book[?(@.price < 10)].title')
print(result)

# 6. 提取价格小于或者等于20的所有商品的价格
result = jsonpath.jsonpath(info, '$..*[?(@.price<=20)].price')
print(result)

# 7. 提取所有书籍的作者信息
result = jsonpath.jsonpath(info, '$.store.book[::].author')
print(result)
result = jsonpath.jsonpath(info, '$.store.book[*].author')
print(result)
result = jsonpath.jsonpath(info, '$..author')
print(result)


# 8. 获取store中所有商品价格信息
result = jsonpath.jsonpath(info, '$.store..price')
print(result)

# 9. 获取带有isbn的书
result = jsonpath.jsonpath(info, '$..book[?(@.isbn)].title')
print(result)

# 10. 获取不带有isbn的书
result = jsonpath.jsonpath(info, '$..book[?(!@.isbn)].title')
print(result)

# 11. 获取价格在5-10这个区间的书籍
result = jsonpath.jsonpath(info, '$..book[?(@.price>=5 && @.price<=10)].title')
print(result)

# 12. 获取价格不在不在5 - 10 这个区间的书籍
result = jsonpath.jsonpath(info, '$..book[?(@.price<5 || @.price>10)].title')
print(result)

# 13. 获取所有元素
result = jsonpath.jsonpath(info, '$..')
print(result)














