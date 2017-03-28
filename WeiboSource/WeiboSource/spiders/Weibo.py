from scrapy.spiders import CrawlSpider


class Weibo(CrawlSpider):
    name = "Weibo"  # 爬虫命名
    start_urls = ['http://movie.douban.com/top250']  # 要爬取的页面地址
    # start_urls = ['http://weibo.com/p/10050583018062']  # 要爬取的页面地址

    def parse(self, response):
        print(response.body)
