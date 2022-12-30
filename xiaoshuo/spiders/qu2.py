# CrawSpider类的使用
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Qu2Spider(CrawlSpider):
    name = 'qu2'
    allowed_domains = ['luoshenol.com']
    # start_urls = ['http://www.luoshenol.com/book/392_392419/159921271.html']
    start_urls = ['http://www.luoshenol.com/book/392_392419/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//*[@id="list"]/dl/dd[13]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'/html/body/div/div[4]/div/div[2]/div[1]/a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        title = response.xpath('//h1/text()').extract_first()
        content = response.xpath('string(//div[@id="content"])').extract_first().strip().replace('    ', '\n')
        yield {
            'title':title,
            'content':content
        }
        # return item
