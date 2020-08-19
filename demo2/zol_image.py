# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 0:19
# @Author  : summer
# @File    : zol_image.py

import urllib3
import re
import time
from multiprocessing.dummy import Pool


"""
http://desk.zol.com.cn/pc/
1. 分析网站，发现数据是静态的在首页的html文件下
2. 模拟请求，访问网站页面，获取html代码
3. 制定规则，提取数据，
4. 访问图片，下载数据
使用multiprocessing线程池下载
"""

#清除urllib3的https警告
urllib3.disable_warnings()

def download_pic(image_info, http_obj):
    resp = http_obj.request("GET", url=image_info[0])
    with open(r"./images/{}.jpg".format(image_info[1]), "wb") as f:
        f.write(resp.data)

    print("[+] '{}'图片下载完毕".format(image_info[1]))


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36"
    }

    url = "http://desk.zol.com.cn/pc/"
    th_pool = Pool()
    http = urllib3.PoolManager(headers=headers)
    http_resp = http.request("GET", url=url)
    resp_text = http_resp.data.decode("GB2312")

    #()re匹配保存,re.S匹配换行
    item_list = re.findall(r'<img width="208px" height="130px"  alt=".*?" src="(.*?)" title = "(.*?)"/>', resp_text, re.S)

    star_time = time.time()
    for item in item_list:
        th_pool.apply_async(func=download_pic, args=(item, http))

    th_pool.close()
    th_pool.join()
    end_time = time.time()
    print("总耗时：{}s".format(end_time - star_time))


if __name__ == '__main__':
    main()












