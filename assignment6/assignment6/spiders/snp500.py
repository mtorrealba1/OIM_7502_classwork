import scrapy

class Sp500Spider(scrapy.Spider):
    name = 'sp500'
    allowed_domains = ['slickcharts.com']
    start_urls = ['https://www.slickcharts.com/sp500/performance']

    def parse(self, response):
        rows = response.xpath('//table[@class="table table-hover table-borderless table-sm"]/tbody/tr')
        for row in rows:
            yield {
                'number': row.xpath('.//td[1]/text()').get(),
                'company': row.xpath('.//td[2]/a/text()').get(),
                'symbol': row.xpath('.//td[3]/a/text()').get(),
                'ytd_return': row.xpath('.//td[last()]/text()').get().strip(' \xa0\xa0')
            }

