# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LofterPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        with open("articles/{}.txt".format(title), "wb") as f:
            f.write(content.encode())
        return item
