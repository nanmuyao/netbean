# _*_ coding:utf-8 _*_
__author__ = 'tars'
_date__ = '2018/5/13 8:26'

import scrapy
from urllib import parse
# from netbean.spiders.spiderNetBean import netBeanUtil

class NetBeanCloud(scrapy.Spider):
    name = "netBeanCloud"
    allowed_domains = ["www.music.163.com"]
    start_urls = [
        "http://music.163.com/artist?id=7763"
    ]

    def parse(self, response):
        post_nodes = response.css('#artist-top50 .f-cb #song-list-pre-cache .f-hide li')
        print(post_nodes)
        url = "https: // music.163.com / weapi / v1 / resource / comments / R_SO_4_26154897?csrf_token ="
        # for post_node in post_nodes:
        #     post_url = post_node.css('a::attr(href)').extract_first()
            # url = parse.urljoin(response.url, post_url)
            # print(post_url)

    def parse_detail(self, response):
        pass



