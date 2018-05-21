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
        'LOG_ENABLED': True,
        'CONCURRENT_REQUESTS': 32,
        'ITEM_PIPELINES': {'netbean.pipelines.CSVPipeline': 5},
    }

    name = 'lianjiaDL'
    allowed_domains = ['dl.lianjia.com']
    start_urls = ['https://dl.lianjia.com/ershoufang/ganjingzi/']

    def __init__(self):
        self.current_page_num = 2
        self.page_count = 30
        self.total_count = 0

    def parse(self, response):
        if (self.total_count == 0):
            self.total_count = int(response.css('h2.total span::text').extract_first())

        post_nodes = response.css(".sellListContent .clear .info")
        for post_node in post_nodes:
            lianjia_item = LianJiaItem()
            item_loader = ArticleItemLoader(item=LianJiaItem(), response=response)
            house_title = post_node.css(".clear .title a::text").extract_first()
            unitPrice = post_node.css(".unitPrice span::text").extract_first()
            total_price = post_node.css(".totalPrice span::text").extract_first()
            hourse_info = post_node.css(".houseInfo::text").extract_first()
            house_url = post_node.css(".title ::attr(href)").extract_first()

            # 这里本来可以用add_css 但是因为遇到了同时有多条数据的情况所以就从post_node先取得node然后在add_value吧
            item_loader.add_value("house_title", house_title)
            item_loader.add_value('house_unit_price', unitPrice)
            item_loader.add_value('total_price', total_price)
            item_loader.add_value('house_url', house_url)
            item_loader.add_value('hourse_info', hourse_info)
            item_loader.add_value('size', hourse_info)
            lianjia_item = item_loader.load_item()
            yield lianjia_item

        # 提取下一页并交给scrapy进行下载
        # 这里可以优化一下每次发送10个请求，因为scrapy可以支持并发请求大大的提高效率
        for index in range(1, 16):
            next_url = "https://dl.lianjia.com/ershoufang/ganjingzi/pg{}/".format(self.current_page_num)
            self.current_page_num = self.current_page_num + 1

            if (self.current_page_num > (self.total_count / self.page_count)):
                print("self.current_page_num=", self.current_page_num)
                self.close_spider()
                return
            if next_url:
                print("并发请求next_url", next_url)
                yield Request(url=parse.urljoin(response.url, next_url), dont_filter=True, callback=self.parse)

    def parase_detail(self, response):
        pass
