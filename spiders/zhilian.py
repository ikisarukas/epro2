# -*- coding: utf-8 -*-
from scrapy import Request
import epro2.spiders.functions as fn
import scrapy



class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://jobs.zhaopin.com/']
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    keywork="python"

    def start_requests(self):
        urls=fn.zl_starturls(self.keywork)
        for i in urls:
            yield Request(i,headers=self.header,meta={'cookiejar':1},callback=self.parse_index)

    def parse_index(self, response):
        # index=response.xpath("//div[@id='listContent']//a[@class='contentpile__content__wrapper__item__info']/@href").extract()
        index = response.xpath("//body").extract()
        print("index====",index)
        for i in index:
            print(i)
