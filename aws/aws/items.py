# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AwsItem(scrapy.Item):
    # define the fields for your item here like:
    region = scrapy.Field()
    name = scrapy.Field()
    vcpu = scrapy.Field()
    ecu = scrapy.Field()
    memory_gib = scrapy.Field()
    internal_storage_gb = scrapy.Field()
    price_per_hour = scrapy.Field()

    pass
