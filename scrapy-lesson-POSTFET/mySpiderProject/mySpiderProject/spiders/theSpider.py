import scrapy, json


class ThespiderSpider(scrapy.Spider):
    name = 'theSpider'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        # post
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 '
                          'Safari/537.36 '
        }
        data = {
            'kw': 'good'
        }
        yield scrapy.Request(url=str(self.start_urls), method='POST', body=json.dumps(data), headers=header)

    def parse(self, response):
        print(response.text)

