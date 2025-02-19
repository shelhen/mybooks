# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 下午9:49
# @Author  : 顾安
# @File    : 5.视频下载并显示进度条.py
# @Software: PyCharm


import requests

# 视频URL
video_url = "https://v95-zj.douyinvod.com/94970136598ac257fc33807d6fdce401/6531441d/video/tos/cn/tos-cn-ve-15c001-alinc2/ooBGZKYCey1IB2L7f9IhBHAGBqAeCx3FL5RQOG/?a=1128&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1181&bt=1181&cs=0&ds=6&ft=blh3-IQQqU-mfJ4ZPo0OW_EklpPiXro0jFVJEl05npvPD-I&mime_type=video_mp4&qs=0&rc=ZDg3Ozo5Omg8ODRkOWQzOUBpang2anc5cmhmbjMzNGkzM0AxLTYzY19iNjAxLjNeNGAxYSNkZmxzMmQ0YWVgLS1kLTBzcw%3D%3D&btag=e000b0001&cc=4a&dy_q=1697723608&l=20231019215328C4913E83B6E00626FBEF"

# 发送请求
r = requests.get(url=video_url, stream=True)

response_body_length = int(r.headers.get("Content-Length"))
print("body的数据长度为:", response_body_length)

# 获取响应内容存储到文件
with open("抖音.mp4", 'wb') as fd:
    write_length = 0
    for chunk in r.iter_content(chunk_size=100):
        write_length += fd.write(chunk)  # write的返回值为写入到文件内容的多少
        print("下载进度: %02.2f%%" % (100 * write_length / response_body_length))
