# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 21:54
# @Author  : summer
# @File    : req_test.py


import requests
import json


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
}

#get方法传递query数据
params = {
    'prod': 'pc_his',
    'from': 'pc_web',
    'json': 1,
}
#post方法传递form表单
data = {
    'username': 'summer',
    'password': 112233,
}
#代理,快代理网站
proxies = {
    'http': 'http://163.204.247.91:9999',
}



resp = requests.get(url="http://httpbin.org/get", headers=headers, proxies=proxies)
# resp = requests.get(url="http://httpbin.org/get", headers=headers, params=params)
# resp = requests.post(url="http://httpbin.org/post", headers=headers, data=data)

# print(resp.headers)
# print(resp.request.headers)
# print(resp.status_code)
print(resp.text)
# print(resp.encoding)
# print(resp.cookies)

# print(type(resp.json()))





