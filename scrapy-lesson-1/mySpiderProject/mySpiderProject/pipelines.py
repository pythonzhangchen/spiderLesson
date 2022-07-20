# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderprojectPipeline:
    def process_item(self, item, spider):
        name = item['name']
        address = item['address']
        with open('aa.txt', 'a', encoding='utf-8') as add:
            add.write(name + address + '\n')
        return item
