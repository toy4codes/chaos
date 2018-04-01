'''
@author: toy4codes
'''

import scrapy
from datetime import date

# PAGE_SIZE = 12
BASE_URL = 'http://chuansong.me/account/'

class ChuanSongMe(scrapy.Spider):

    def start_requests(self):
        urls = [
            BASE_URL + self.name
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        articles = response.css('a[class="question_link"]')
        with open(self.filename, 'a', encoding='UTF-8') as file:
            for article in articles:
                article_title = article.css('a::text').extract_first().strip()
                article_href = response.urljoin(article.css('a::attr("href")').extract_first())
                file.write('%s\n' % article_title)
                yield {
                    'article_title': article_title,
                    'article_href': article_href
                }
        
        # follow pagination links
        for href in response.css('a[style="float: right"]::attr("href")'):
            yield response.follow(href, self.parse)

class DBDevs(ChuanSongMe):
    name = 'DBDevs'
    filename = 'DBDevs' + '-' + str(date.today()) + ".txt"

class ImportNew(ChuanSongMe):
    name = 'importnew'
    filename = 'importnew' + '-' + str(date.today()) + ".txt"

class BigData(ChuanSongMe):
    name = 'TheBigData1024'
    filename = 'TheBigData1024' + '-' + str(date.today()) + ".txt"

class IProgrammer(ChuanSongMe):
    name = 'iProgrammer'
    filename = 'iProgrammer' + '-' + str(date.today()) + ".txt"

class PythonCoder(ChuanSongMe):
    name = 'PythonCoder'
    filename = 'PythonCoder' + '-' + str(date.today()) + ".txt"

class LinuxHub(ChuanSongMe):
    name = 'LinuxHub'
    filename = 'LinuxHub' + '-' + str(date.today()) + ".txt"

class Jobbole(ChuanSongMe):
    name = 'jobbole'
    filename = 'jobbole' + '-' + str(date.today()) + ".txt"

class FrontDev(ChuanSongMe):
    name = 'FrontDev'
    filename = 'FrontDev' + '-' + str(date.today()) + ".txt"

class Operation(ChuanSongMe):
    name = 'Operation1024'
    filename = 'Operation1024' + '-' + str(date.today()) + ".txt"

class TheAlgorithm(ChuanSongMe):
    name = 'TheAlgorithm'
    filename = 'TheAlgorithm' + '-' + str(date.today()) + ".txt"

class KanXue(ChuanSongMe):
    name = 'ikanxue'
    filename = 'ikanxue' + '-' + str(date.today()) + ".txt"

class HackerCoder(ChuanSongMe):    
    name = 'HackerCoder'
    filename = 'HackerCoder' + '-' + str(date.today()) + ".txt"
    
class PhpDevs(ChuanSongMe):
    name = 'phpDevs'
    filename = 'phpDevs' + '-' + str(date.today()) + ".txt"

class ITLog(ChuanSongMe):
    name = 'IT_log'
    filename = 'IT_log' + '-' + str(date.today()) + ".txt"

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    process.crawl(DBDevs)
    process.crawl(ImportNew)
    process.crawl(BigData)
    process.crawl(IProgrammer)
    process.crawl(PythonCoder)
    process.crawl(LinuxHub)
    process.crawl(Jobbole)
    process.crawl(FrontDev)
    process.crawl(Operation)
    process.crawl(TheAlgorithm)
    process.crawl(KanXue)
    process.crawl(HackerCoder)
    process.crawl(PhpDevs)
    process.crawl(ITLog)
    process.start()
    