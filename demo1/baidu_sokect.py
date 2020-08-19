# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 21:27
# @Author  : summer
# @File    : baidu_sokect.py

import socket
import time

#1.创建socket对象
conn = socket.socket()

#2.连接到指定主机
conn.connect(("www.baidu.com", 80))

#3.创建HTTPq请求报文数据
#百度首页是HTTPS，本来直接访问是不行的，但是百度有点bug，访问baidu.com
send_data = b'''GET / HTTP/1.1\r\nHost: baidu.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36\r\n\r\n'''

#4.发送请求报文
conn.send(send_data)

#5.循环接收服务器返回数据
while True:
    temp = conn.recv(1024)
    time.sleep(0.1)
    print(temp.decode(encoding="UTF-8"))
    if len(temp) < 1024:
        conn.close()
        break




