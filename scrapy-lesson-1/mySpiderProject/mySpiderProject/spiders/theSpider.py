import scrapy
from mySpiderProject.items import MyspiderprojectItem


class ThespiderSpider(scrapy.Spider):
    name = 'theSpider'  # 爬虫器的名字，不建议修改
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['https://xa.fang.ke.com/loupan/']

    # todo 一次调用
    # def parse(self, response):
    #     main_li_list = response.xpath('/html/body/div[6]/ul[2]/li')     # bs4 re
    #     # print(main_li_list)
    #     # print(len(main_li_list))
    #     for li in main_li_list:
    #         name = li.xpath('./a/@title').extract()[0]
    #         address = li.xpath('./div/a[1]/text()').extract()[-1].strip()
    #         # print(name,address)
    #         items = MyspiderprojectItem()
    #         items['name']= name
    #         items['address']=address
    #
    #         yield items

    # todo 第一阶段  多次调用 多页
    page_number = 1
    start_urls = ['https://xa.fang.ke.com/loupan/pg%s/' % page_number]
    base_url = 'https://xa.fang.ke.com/loupan/pg%s/'

    #
    # def parse(self, response):
    #     main_li_list = response.xpath('/html/body/div[6]/ul[2]/li')
    #     for li in main_li_list:
    #         name = li.xpath('./a/@title').extract()[0]
    #         address = li.xpath('./div/a[1]/text()').extract()[-1].strip()
    #         print(name, address)
    #         if self.page_number <= 3:
    #             self.page_number = self.page_number + 1
    #             new_url = self.base_url % self.page_number
    #             yield scrapy.Request(url=new_url, callback=self.parse)

    # todo 第二阶段  完成页面  一个页面全部数据的穿透，注意这里的数据被分割了
    # def detail_page_parse(self, response):
    #     item = response.meta['item']
    #     nickname = response.xpath('//*[@class="other-name"]/text()').extract()[-1].strip()
    #     item['nickname'] = nickname
    #     yield item
    #
    # def parse(self, response):
    #     main_li_list = response.xpath('/html/body/div[6]/ul[2]/li')
    #     for li in main_li_list:
    #         name = li.xpath('./a/@title').extract()[0]
    #         address = li.xpath('./div/a[1]/text()').extract()[-1].strip()
    #         link = 'https://xa.fang.ke.com/' + li.xpath('./a/@href').extract_first()
    #         item = MyspiderprojectItem()
    #         item['name'] = name
    #         item['address'] = address
    #         item['link'] = link
    #         # print(name, address, link)
    #         yield scrapy.Request(url=link, callback=self.detail_page_parse, meta={'item': item})

    # todo 第三阶段  联合多页面  以及详情页面的 闭环爬取
    def detail_page_parse(self, response):
        item = response.meta['item']
        try:
            nickname = response.xpath('//*[@class="other-name"]/text()').extract()[-1].strip()
        except:
            nickname = '别名：N/A'
        item['nickname'] = nickname
        yield item

        if self.page_number <= 4:
            self.page_number += 1
            new_link = self.base_url % self.page_number
            print('******************', new_link, '***********************')
            yield scrapy.Request(url=new_link, callback=self.parse)

    def parse(self, response):
        main_li_list = response.xpath('/html/body/div[6]/ul[2]/li')
        for li in main_li_list:
            name = li.xpath('./a/@title').extract()[0]
            address = li.xpath('./div/a[1]/text()').extract()[-1].strip()
            link = 'https://xa.fang.ke.com/' + li.xpath('./a/@href').extract_first()
            item = MyspiderprojectItem()
            item['name'] = name
            item['address'] = address
            item['link'] = link
            # print(name, address, link)
            yield scrapy.Request(url=link, callback=self.detail_page_parse, meta={'item': item})
