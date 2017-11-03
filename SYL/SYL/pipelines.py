# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from SYL.models import Repository,engine
from SYL.items import SylItem

class SylPipeline(object):
    def process_item(self, item, spider):
        #self._process_syl_item(item)
        #return item
    
    #def _process_syl_item(self,item):
        #item['name'] = item['name']
        #item['update_time'] = item['update_return']
        self.session.add(Repository(**item))
        return item
        #self.session.add(SylItem(**item))
        
    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
