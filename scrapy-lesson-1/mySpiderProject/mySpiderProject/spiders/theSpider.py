import scrapy
from mySpiderProject.items import MyspiderprojectItem

class ThespiderSpider(scrapy.Spider):
    name = 'theSpider'      # 爬虫器的名字，不建议修改
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://xa.fang.ke.com/loupan/']

    def parse(self, response):
        main_li_list = response.xpath('/html/body/div[6]/ul[2]/li')     # bs4 re
        # print(main_li_list)
        # print(len(main_li_list))
        for li in main_li_list:
            name = li.xpath('./a/@title').extract()[0]
            address = li.xpath('./div/a[1]/text()').extract()[-1].strip()
            # print(name,address)
            items = MyspiderprojectItem()
            items['name']= name
            items['address']=address

            yield items
