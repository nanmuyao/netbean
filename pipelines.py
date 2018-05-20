# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import CsvItemExporter
from scrapy import signals



class NetbeanPipeline(object):
    def process_item(self, item, spider):
        return item


class CSVPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        # file = open('%s_items.csv' % spider.name, 'w+b')
        file = open('lianjia_items.csv', 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = ['house_title', 'house_unit_price']
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.files[spider] = self.files.pop(spider)
        self.files[spider].close()

    def process_item(self, item, spider):
        if self.exporter:
            self.exporter.export_item(item)
        return item
