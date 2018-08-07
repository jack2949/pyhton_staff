# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from collections import OrderedDict

class LaughPipeline(object):
    count = 1

    def __init__(self):
        self.file = codecs.open('data_utf8_niuren1.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        print str(self.count) + ' PIPE OK! ' + item['name']
        print str(self.count) + ' PIPE OK! ' + item['path']
        self.count = self.count + 1
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
