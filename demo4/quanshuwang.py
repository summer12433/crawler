# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 23:56
# @Author  : summer
# @File    : quanshuwang.py

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}

resp = requests.get(url="https://www.xs4.cc/0_1/", headers=headers)
resp.encoding = 'gbk'
html = etree.HTML(resp.text)
#normalize-space去掉空格
print(html.xpath('normalize-space(//div[@id="intro"]/p/text())'))
print(html.xpath('//div[@id="info"]/h1/text()'))
