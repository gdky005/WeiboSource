from scrapy import Selector
from scrapy.spiders import CrawlSpider


class Weibo(CrawlSpider):
    name = "Weibo"  # 爬虫命名
    # start_urls = ['http://weibo.cn/pub']  # 要爬取的页面地址
    start_urls = ['http://movie.douban.com/top250']  # 要爬取的页面地址
    # start_urls = ['http://weibo.com/p/10050583018062']  # 要爬取的页面地址

    def parse(self, response):
        print(response.body.decode('utf-8'))

        # selector = Selector(response)
        #
        # Movies = selector.xpath('//div[@class="info"]')
        #
        # for eachMovie in Movies:
        #     title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
        #     full_title = ''
        #     for each in title:
        #         full_title += each
        #
        #     movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
        #     movieDetail = ''
        #     for movieInfo in movieInfo:
        #         movieDetail += movieInfo
        #
        #     start = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[
        #         0]
        #
        #     quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
        #     if quote:
        #         quote = quote[0]
        #     else:
        #         quote = ""
        #
        #     print(full_title + "\n")
        #     print(movieDetail + "\n")
        #     print(start + "\n")
        #     print("\n""\n""\n经常绝伦的言论： " + quote + "\n""\n""\n")
        #
        #     break  #先显示一个，如果要全部显示，可以注释这个 break



