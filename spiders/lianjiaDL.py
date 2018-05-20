# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import logging
import scrapy.settings
from netbean.items import LianJiaItem, ArticleItemLoader

class LianjiadlSpider(scrapy.Spider):
    custom_settings = {
        'DOWNLOAD_DELAY': '0',
        'LOG_ENABLED' : True,
        'ITEM_PIPELINES' : {'netbean.pipelines.CSVPipeline':5},
    }

    current_page_num = 2
    name = 'lianjiaDL'
    allowed_domains = ['dl.lianjia.com']
    start_urls = ['https://dl.lianjia.com/ershoufang/ganjingzi/']

    def parse(self, response):
        post_nodes = response.css(".sellListContent .clear .info")
        for post_node in post_nodes:
            lianjia_item = LianJiaItem()
            item_loader = ArticleItemLoader(item=LianJiaItem(), response=response)
            house_title = post_node.css(".clear .title a::text").extract_first()
            unitPrice = post_node.css(".unitPrice span::text").extract_first()
            item_loader.add_value("house_title", house_title)
            item_loader.add_value('house_unit_price', unitPrice)
            lianjia_item = item_loader.load_item()
            yield lianjia_item

        # 提取下一页并交给scrapy进行下载
        next_url = "https://dl.lianjia.com/ershoufang/ganjingzi/pg{}/".format(self.current_page_num)
        self.current_page_num = self.current_page_num + 1
        if (self.current_page_num > 30) :
            print("self.current_page_num=", self.current_page_num)
            self.close_spider()
            return
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), dont_filter=True, callback=self.parse)

    def parase_detail(self, response):
        pass




