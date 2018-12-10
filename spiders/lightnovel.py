# -*- coding: utf-8 -*-
import scrapy
import threading
import epro2.epro2.mythread as mythread
import redis
from epro2.epro2.settings import pages
import epro2.epro2.spiders.functions as fn
from epro2.epro2.items import LightnovelItem


class LightnovelSpider(scrapy.Spider):
    name = 'lightnovel'
    r=fn.conredis()
    r2=fn.conredis()
    allowed_domains = ['lightnovel.cn']
    start_urls = ['https://www.lightnovel.cn/forum-96-1.html',
                  'https://www.lightnovel.cn/forum-4-1.html',
                  'https://www.lightnovel.cn/forum-173-1.html']
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }

    def start_requests(self):
        infoclass=('news','latestnovel','novel')
        print("###########开始爬取列表##########")
        t1=threading.Thread(target=fn.urltoredis,args=(self.r,infoclass))
        t1.start()
        print('t1开始------------------')

        t2=mythread.MyThread(fn.urlfromredis,args=(self.r2,infoclass,),name=fn.urlfromredis.__name__)
        t2.start()
        print('t2开始------------------')
        t1.join()
        t2.join()
        print('t2  join开始------------------')
        result=t2.get_result()
        print('tuple  result is  -------',result)
        for item in result:
            print('iiiiiiiiiiiiiiiiiiiii=',item)
            # print('0===',item[0])
            # print('1===', item[1])
            for j in item[0]:
                print(j)
                yield scrapy.Request(url=j, meta={'url': j,'infoclass':item[1]}, callback=self.parse
                             )

        #
        # t2.start()
        # print('t2开始------------------')
        # t2.join()


    def parse(self, response):
        infoclass=response.meta['infoclass']
        print('parse url is -------',infoclass)
        category = response.xpath("//tbody[starts-with(@id,'normalthread')]/tr/th/em/a/text()").extract()
        title=response.xpath("//tbody[starts-with(@id,'normalthread')]//a[@class='s xst']/text()").extract()
        url_part1=response.xpath("//tbody[starts-with(@id,'normalthread')]//a[@class='s xst']/@href").extract()
        url=fn.ln_title_url(url_part1)

        # for i in url:
        #     print('partern_url=',i)
        item=LightnovelItem()
        item['category']=category
        item['title']=title
        item['url']=url
        item['infoclass']=infoclass
        return item

