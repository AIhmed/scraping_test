# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

class IceteaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags),output_processor=TakeFirst())
    breadcrumbs=scrapy.Field(input_processor=MapCompose(remove_tags),output_processor=TakeFirst())

