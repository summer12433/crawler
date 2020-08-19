# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PadoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    cover_url = scrapy.Field()
    movie_url = scrapy.Field()
    release_date = scrapy.Field()
    types = scrapy.Field()
    regions = scrapy.Field()
    actors = scrapy.Field()
    score = scrapy.Field()
