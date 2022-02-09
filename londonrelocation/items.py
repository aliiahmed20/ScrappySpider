# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import Takefirst, MapCompose



class LondonrelocationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
