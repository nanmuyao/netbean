# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import re

class NetbeanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ArticleItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()
    # default_input_processor = TakeFirst()


# def show_input(value):
#     print(value)
#     pass
#
#
# def show_output(value):
#     print(value)
#     pass


def get_hourse_size(value):
    # match_re = re.match(r'\d+\.\d+', value)
    # if match_re:
    #     nums = int(match_re.group(1))
    # else:
    #     nums = 0
    # return nums
    pattern = re.compile(r'\d+\.\d+')
    match_re = pattern.search(value)
    if match_re:
        print(match_re.group(0))
        content = match_re.group(0)
        nums = float(match_re.group(0))
    else:
        nums = 0
    return nums


# 链家item
class LianJiaItem(scrapy.Item):
    house_title = scrapy.Field(
        # output_processor=MapCompose(show_output),
        # input_processor=MapCompose(show_input)
    )
    house_unit_price = scrapy.Field()
    hourse_info = scrapy.Field()
    house_url = scrapy.Field()
    total_price = scrapy.Field()
    size = scrapy.Field(
        input_processor=MapCompose(get_hourse_size)
    )

