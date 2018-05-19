# _*_ coding:utf-8 _*_
__author__ = 'tars'
_date__ = '2018/5/13 8:31'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "netBeanCloud"])
