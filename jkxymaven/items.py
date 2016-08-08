# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class JkxymavenItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ''' 对爬取到的数据在这里面先进行定义
    '''
    title = Field()
    # movieInfo = Field()
    videolessonfilename = Field()