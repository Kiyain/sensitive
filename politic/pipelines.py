# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import json
# import pymysql


class PoliticPipeline(object):
    def process_item(self, item, spider):
        # 获取当前工作目录
        base_dir = os.getcwd()
        file_name = base_dir + "/news.json"
        # 从内存以追加的方式打开文件，并写入相应的数据
        # with open(file_name,'a') as f:
        #     f.write(item['link'] + ' ' + item['time'] + ' ' + item['title'] + ' ' + item['label'])
        with codecs.open(file_name, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item
