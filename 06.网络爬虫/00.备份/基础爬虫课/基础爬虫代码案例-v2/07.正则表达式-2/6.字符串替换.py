# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.字符串替换.py
# @Software: PyCharm
# @Time    : 2023/10/31 20:52


import re

html_obj = '''

下面是这学期要学习的课程：

<a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是牛顿第2运动定律

<a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是毕达哥拉斯公式

<a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是切割磁力线
'''


data = re.sub(r'/av\d+/', '/cn34567/', html_obj)
print(data)


