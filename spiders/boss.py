# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import epro2.epro2.spiders.functions as fn


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['http://zhipin.com/']
    url = 'http://zhipin.com'

    def start_requests(self):
        fn.test(self.url,self.parse)
        # yield Request(url=self.url,callback=self.parse
        #     )
    def parse(self, response):
        pass
