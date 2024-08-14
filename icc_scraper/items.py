# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StationItem(scrapy.Item):
    label = scrapy.Field()
    value = scrapy.Field()

class VariableItem(scrapy.Item):
    label = scrapy.Field()
    value = scrapy.Field()

class GroupItem(scrapy.Item):
    label = scrapy.Field()
    value = scrapy.Field()


class IccScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
