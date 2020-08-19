# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 22:42
# @Author  : summer
# @File    : urllib_test.py

from urllib import request
from urllib import error
from urllib import parse


#不设置data的urlopen是get方法
#若发送post请求，设置data
# resp = request.urlopen(url="http://httpbin.org/get")
# resp = request.urlopen(url="http://httpbin.org/post", data=b'username=summer')
# try:
#     resp = request.urlopen(url="http:/www.youtube.com/", timeout=2)
# except error.URLError as e:
#     print("报错了:{}".format(e))
# print(dir(resp))  #查看返回内容得属性
# print(resp.status)  #查看状态码
# print(resp.read().decode("UTF8"))  #查看返回内容
# print(resp.url)  #查看网址
# print(resp.headers)  #查看请求头部信息


#request 模块
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
# }
# req = request.Request(url="http://httpbin.org/get", headers=headers)
# resp = request.urlopen(req)
# print(resp.read().decode("UTF8"))


#parse 模块
params = {
    "name": "张三",
    "年龄": "十八",
}
front_url = parse.urlencode(params)
url = "http://www.baidu.com/s?"
print(url + front_url)
print(parse.parse_qs(front_url))










