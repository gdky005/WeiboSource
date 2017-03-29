from scrapy import FormRequest
from scrapy import Selector
from scrapy.spiders import CrawlSpider


class Weibo(CrawlSpider):
    name = "Weibo"  # 爬虫命名
    # start_urls = ['http://weibo.cn/pub']  # 要爬取的页面地址
    # start_urls = ['http://movie.douban.com/top250']  # 要爬取的页面地址
    start_urls = ['http://weibo.com/p/10050583018062']  # 要爬取的页面地址

    def start_requests(self):
        cookies = {"SINAGLOBAL": "6109691141173.243.1438072255386",
                   "_ga": "GA1.2.2073578723.1457689189",
                   "__gads": "ID",
                   "YF-Ugrow-G0": "ad06784f6deda07eea88e095402e4243",
                   "YF-V5-G0": "c37fc61749949aeb7f71c3016675ad75",
                   "_s_tentry": "login.sina.com.cn",
                   "Apache": "8319853895847.242.1490687179455",
                   "ULV": "1490687179779:150:5:1:8319853895847.242.1490687179455:1489573390792",
                   "YF-Page-G0": "e44a6a701dd9c412116754ca0e3c82c3",
                   "login_sid_t": "cbafa21194854406fba7980d30b354be",
                   "UOR": "blog.csdn.net,widget.weibo.com,login.sina.com.cn",
                   "WBStorage": "02e13baf68409715|undefined",
                   "SCF": "Aof0G5U0IYtGXakUN5rDtjMpG63xnPsfAGHAI56omax6JTrFNqPjZLKD3aVioESJ-uZqwtyXBHJi4LITefy1nl0.",
                   "SUB": "_2A2513yOwDeRxGedJ7lIR8ifOzDiIHXVWrRJ4rDV8PUNbmtBeLVjakW86aca01a4BFS9OxcgGLC_iwos-6w..",
                   "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WWdYaRAKqagDyKVOZec8i675JpX5K2hUgL.Fo2NSK57eo.ES0B2dJLoIEBLxK-LB-BLBKBLxKML12zLB-eLxKML12zL1hzLxK.LBK-LB--t",
                   "SUHB": "0ebcuqHxxLAQ9V",
                   "ALF": "1522304863",
                   "SSOLoginState": "1490768864",
                   "un": "gdky005@126.com",
                   "wvr": "6"}
        return [FormRequest(self.start_urls[0], cookies=cookies, callback=self.parse)]

    def parse(self, response):
        print(response.body.decode('utf-8'))

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
