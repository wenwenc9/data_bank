# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaocheItem(scrapy.Item):
    # define the fields for your item here like:
    car_title = scrapy.Field()
    car_now_price = scrapy.Field()
    car_old_price = scrapy.Field()
    car_years = scrapy.Field()
    car_product_area = scrapy.Field()
    car_licheng = scrapy.Field()
    ip = scrapy.Field()
    car_url = scrapy.Field()
    car_id = scrapy.Field()
