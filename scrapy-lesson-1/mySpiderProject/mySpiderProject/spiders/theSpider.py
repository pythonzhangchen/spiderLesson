import scrapy


class ThespiderSpider(scrapy.Spider):
    name = 'theSpider'      # 爬虫器的名字，不建议修改
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print(response.text)
        pass
