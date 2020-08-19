# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class PadoubanPipeline:
    #定义爬虫开始运行执行，打开文件
    def open_spider(self, spider):
        self.file = open(r"dou.json", "w")

    #爬虫把数据发送给管道调用
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    #定义爬虫关闭运行执行，关闭文件
    def close_spider(self, spider):
        self.file.close()