# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 22:21
# @Author  : summer
# @File    : img_download.py

import socket
import time
import re

#1 建立链接
conn = socket.socket()

#2 设置链接目标
conn.connect(("111.10.29.168", 80))

#3报文设置
http_req = b'''\
GET /files/pic/pic9/202007/hpic2755.jpg HTTP/1.1\r\n\
HOST: http://pic.sc.chinaz.com\r\n\
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36\r\n\
Referer: no-referrer-when-downgrade\r\n\r\n
'''

conn.send(http_req)
http_resq = b''
temp = conn.recv(1024)
http_resq += temp
content_len = re.findall(b"\r\nContent-Length:(.*?)\r\n",temp)[0]
num = int(content_len) // 1024 + 1
while True:
    temp = conn.recv(1024)
    http_resq += temp
    time.sleep(0.1)
    num -= 1
    if not num:
        conn.close()
        break

pic_data = http_resq.split(b'\r\n\r\n')[1]

with open(r"pic.png", "wb") as f:
    f.write(pic_data)


print(http_resq)








