# -*- coding: utf-8 -*-
import scrapy


class HousespiderSpider(scrapy.Spider):
    name = 'housespider'

    headler = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '  
                      'Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    start_urls = ['http://www.creprice.cn/rank/index/parms/eyJkaSI6ImFsbCIsInBpIjoiYmVpamluZyIsImNpIjoiYmoiLCJwdCI6MTEsInR5Ijoic2FsZSIsInVuIjoiZGlzdHJpY3QiLCJpbiI6IlByaWNlIiwibW4iOiIyMDE4LTEwIn0%3D.html']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headler)

    def parse(self, response):
        ci = 2
        pi = 2
        pri = 2
        for i in range(31):
            c='/html/body/div[2]/div[4]/table/tbody/tr['+str(i)+']'
            yield {
				"date":response.xpath(c+'/td[1]').extract_first(),
				"p1":response.xpath(c+'/td[2]').extract(),
				"p2":response.xpath(c+'/td[3]').extract(),
				"p3":response.xpath(c+'/td[4]').extract(),
				"p4":response.xpath(c+'/td[5]').extract(),
				"p5":response.xpath(c+'/td[6]').extract(),
				"p6":response.xpath(c+'/td[7]').extract(),
				"p7":response.xpath(c+'/td[8]').extract(),
				"p8":response.xpath(c+'/td[9]').extract(),
				"p9":response.xpath(c+'/td[10]').extract(),
				"p10":response.xpath(c+'/td[11]').extract(),
            }
            ci=ci+1
            pi=pi+1
            pri=pri+1

			//*[@id="date"]/s elect[2]/option[4]