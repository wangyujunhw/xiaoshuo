# scrapy.Spider类的使用
import scrapy


class QuSpider(scrapy.Spider):
    name = 'qu'
    allowed_domains = ['luoshenol.com']
    start_urls = ['http://www.luoshenol.com/book/392_392419/159921271.html']
    # start_urls = ['http://www.luoshenol.com/book/392_392419/160095016_4.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = response.xpath('string(//div[@id="content"])').extract_first().strip().replace('    ', '\n')
        # next_url = response.xpath('//*[@id="wrapper"]/div[5]/div/div[2]/div[1]/a[4]/@href').extract_first()
        # next_url = response.xpath('//*[@id="wrapper"]/div[5]/div/div[2]/div[1]/a[4]/@href').extract_first()
        # 如下从xpath插件中拷贝的路径中，其中第二个div的下标和response.xpath解析的下标不一致，导致解析不到相应的连接
        # 在xpath插件中，拷贝该路径：/html/body/div/div[5]/div/div[2]/div[1]/a[4]/@href 在插件中解析没有问题，正确
        # 在py函数中，使用response.xpath('/html/body/div/div[5]/div/div[2]/div[1]/a[4]/@href')就解析不到，需要把修改成如下的方式才可以
        # 在py函数中，使用response.xpath('/html/body/div/div[5]/div/div[2]/div[1]/a[4]/@href')才能够解析到，两者其实差了1；可能是下标起始值不同造成的；
        next_url = response.xpath('/html/body/div/div[4]/div/div[2]/div[1]/a[4]/@href').extract_first()

        # next_url = response.xpath('//div[@class="bottem1"]/a[4]/@href').extract_first()
        print('当前的response是：', response)
        print('下一个url是:', next_url)
        print('join之后的url是：', response.urljoin(next_url))

        yield {
            'title': title,
            'content': content
        }
        yield scrapy.Request(response.urljoin(next_url), callback=self.parse)