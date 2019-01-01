# -*- coding: utf-8 -*-
import  pymysql
from epro2.settings import dbhost,user,password,db
import epro2.items as items
from epro2.spiders.functions import sqlpara


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Epro2Pipeline(object):
    def __init__(self,):
        self.conn=pymysql.connect(host=dbhost,user=user,passwd=password,db=db,use_unicode=True,charset="utf8")
    def process_item(self, item, spider):
        # print('get to pipeline -----------------')
        if(isinstance(item,items.LightnovelItem)):
            category=item['category']
            title = item['title']
            url = item['url']
            infoclass=item['infoclass']
            sqllist=sqlpara(category,title,url)
            # print(sql)
            for i in sqllist:
                sql="insert into "+infoclass+" (category,title,url) values ("+i+")"
                print(sql)
                self.conn.query(sql)
                self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()