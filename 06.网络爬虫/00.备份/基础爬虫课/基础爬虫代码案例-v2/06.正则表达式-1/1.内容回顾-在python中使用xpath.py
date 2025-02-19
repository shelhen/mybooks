# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.内容回顾-在python中使用xpath.py
# @Software: PyCharm
# @Time    : 2023/10/29 20:01


from lxml import etree


text = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''

# 1.创建element对象来使用xpath语法
tree = etree.HTML(text)
# print(tree)

# 可以将element对象转为一个字符串
# print(etree.tostring(tree).decode())

# 2.根据条件获取指定标签
a_list = tree.xpath('//li[@class="item-1"]/a')  # 返回的不是标签 是对象！！！
# print(a_list)

# for item in a_list:
#     # . 代表的是当前标签
#     # 只有element对象才能使用xpath方法
#     # print(item.xpath('./text()'))
#     # print(item.xpath('./@href'))
#     info = dict()
#     info['title'] = item.xpath('./text()')[0]  # xpath方法返回的数据类型是一个列表
#     info['href'] = item.xpath('./@href')[0]
#     print(info)

li_list = tree.xpath('//li[@class="item-1"]')

for li in li_list:
    item = dict()
    item['href'] = li.xpath('./a/@href')[0] if len(li.xpath('./a/@href')) > 0 else '空'
    item['text'] = li.xpath('./a/text()')[0] if len(li.xpath('./a/text()')) > 0 else '空'
    print(item)


"""
将多个同学分为一个组
    男同学一组
    女同学一组
    
以上代码首先获取的是所有的li标签, 当前返回的是一个包含所有li标签对象的列表
    li是不是包含了a标签？ 相当于获取到了所有的a标签？
    li标签和a标签有没有对应关系？
"""





