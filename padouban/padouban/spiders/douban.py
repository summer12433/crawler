import scrapy
import json
from padouban.items import PadoubanItem
class DoubanSpider(scrapy.Spider):
    #爬虫名
    name = 'douban'
    #允许的域名
    allowed_domains = ['movie.douban.com']
    #开始爬取的url
    start_urls = ['https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20']
    #for循环设置
    offset = 0

    #解析引擎返回的响应
    def parse(self, response):
        list_data = json.loads(response.text)
        item = PadoubanItem()
        #判断返回的响应有没有数据，没有就结束爬虫
        if not list_data:
            return

        for i in list_data:
            #item填写自己定义的item，iget填写网页源码的数据
            item["title"] = i.get("title")
            item["cover_url"] = i.get("cover_url")
            item["movie_url"] = i.get("url")
            item["release_date"] = i.get("release_date")
            item["types"] = i.get("types")
            item["regions"] = i.get("regions")
            item["actors"] = i.get("actors")
            item["score"] = i.get("score")
            item["score"] = i.get("score")
            yield item
        #跟进每一页的20条请求
        self.offset += 20
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20".format(self.offset)

        #yield 跟进请求返回url
        yield scrapy.Request(url=url, callback=self.parse)




