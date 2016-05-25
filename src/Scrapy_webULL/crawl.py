from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapy.spider import BaseSpider
from scrapy import log
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import urlparse


# scrapy runspider -s DEPTH_LIMIT=2 crawl.py `-o dataULL.json

class ExampleSpider(CrawlSpider):
    
    filename = "ull.txt"
    #arquivo = open(filename, 'wb')
    name = "example.com"
    allowed_domains = ["ull.es"]
    start_urls = ["http://www.ull.es/"]
    
   
    rules = [Rule(SgmlLinkExtractor(allow=[r'ull.es']), callback='parse_item', follow=True)]
    
    def parse_item(self,response):
        
        #self.log('A response from %s just arrived!' % response.url)
        
        #print response
        for url in response.css('body a::attr(href)'):
            #link = url.xpath('@href').extract()
            full_url = response.urljoin(url.extract())
            extensions = [".png",".jpeg",".svg",".ogg", ".oga" ,".ogv",".txt",".vorbis",".flac",".pdf", ".odt",".ods",".odp",".doc",".xls",".ppt",".docx",".xlsx",".pptx",".mpeg",".mpg",".mp3",".mp4",".aac"]
            for extension in extensions:
                if extension in full_url:
                        #self.arquivo.writelines("%s" % full_url)
                        yield {
                            'Extension': extension,
                            'Url_Full': full_url,
                            'Url_Base': urlparse.urlsplit(full_url)[1],
                            'Filename': (full_url.split('/')[-1]).split('.')[0],
                        }
            
            yield Request(full_url, callback=self.parse_item)
        
   
        #for sel in response.xpath('//a'):
            #print sel
           
            