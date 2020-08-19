# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 21:53
# @Author  : summer
# @File    : 12306_login.py

import requests
from urllib3 import disable_warnings
import re
import base64
from demo3 import user_pass

disable_warnings()

#验证码图片坐标
def position_count(args):
    """
    1 2 3 4
    5 6 7 8
    :param args:
    :return:
    """
    position_dict = {
        '1': '49,50',
        '2': '106,50',
        '3': '174,50',
        '4': '240,50',
        '5': '50,121',
        '6': '120,120',
        '7': '174,123',
        '8': '240,125',
    }
    position_data = []
    for i in args:
        position_data.append(position_dict.get(i))
    return ','.join(position_data)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
}
params = {
    "login_site": "E",
    "module": "login",
    "rand": "sjrand",
    "1554991753795": "",
    "callback": "jQuery19109501439403331622_1554991526443",
    "_": "1554991526445",
}
# 1. 创建session对象, 设置相关信息
session = requests.Session()
session.headers = headers
session.params = params

# 2. 发送请求, 是session不用管cookies
resp = session.get(url="https://kyfw.12306.cn/passport/captcha/captcha-image64", verify=False)

# 3. 数据处理
b64_image = re.findall(r'{"image":"(.*?)",', resp.text, re.S)[0]
image_data = base64.b64decode(b64_image)
with open(r"ca.jpg", "wb") as f:
    f.write(image_data)

# 4. 坐标整理
input_data = input("enter:")
pic_num = input_data.split()
pix_num = position_count(pic_num)
params = {
    "callback": "jQuery19107793119804911866_1554992766399",
    "answer": pix_num,
    "rand": "sjrand",
    "login_site": "E",
    "_": "1554992766402",
}

# 5. 发送check
session.params = params
resp = session.get(url="https://kyfw.12306.cn/passport/captcha/captcha-check", verify=False)
print(resp.text)

data = {
    "username": user_pass.username,
    "password": user_pass.password,
    "appid": "otn",
    "answer": pix_num,
}

session.cookies.update({
    "RAIL_EXPIRATION": "1597303123128",
    "RAIL_DEVICEID": "cslJebgpXjZ-zGvdx4x_vB8AqkPb3pcte_3zwPhvE8_XZaKP-3JhCBse93rG9JUk7hy_X5LI9CNxXLdnCkhmUkrz4FJ4SJSHwV4vT88-hx7QpeUQplsAocT4oPdC1F7LLS--Ph57Wd9XTlIi0IWHxFH84l_ngXM4",
    "route": "9036359bb8a8a461c164a04f8f50b252",
})
print(session.cookies)
resp_login = session.post(url="https://kyfw.12306.cn/otn/resources/login.html", data=data, verify=False)
resp_login.encoding = "UTF-8"
print(resp.text)
