# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    extraction_date = scrapy.Field()
    shop_name = scrapy.Field()
    id = scrapy.Field()
    product_name = scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
    url = scrapy.Field()
    images = scrapy.Field()
