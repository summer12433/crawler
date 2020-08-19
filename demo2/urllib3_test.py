# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 23:10
# @Author  : summer
# @File    : urllib3_test.py


import urllib3


# http = urllib3.PoolManager()
# # resp = http.request("GET", "http://httpbin.org/get")
# resp = http.request("POST", "http://httpbin.org/post", fields={"name": "summer"})
# print(resp.data.decode())
# print(resp.status)
# print(resp.headers)
# print(resp.headers["Date"])

#编写**Query 参数
http = urllib3.PoolManager()
resp = http.request("GET", "http://httpbin.org/get", fields={"image": ""})
print(resp.data.decode())










