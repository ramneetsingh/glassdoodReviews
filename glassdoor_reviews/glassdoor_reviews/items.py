# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassdoorReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    review = scrapy.Field()
    company = scrapy.Field()
    country = scrapy.Field()
    reviews = scrapy.Field()
