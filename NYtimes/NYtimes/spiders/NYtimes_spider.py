import scrapy
from NYtimes.items import NYtimesItem

class NYtimesSpider(scrapy.Spider):
	name = "NYtimes"
	allowed_domains = ["nytimes.com"]
	#start_urls = []
	#for x in xrange(1860,1865):
	#	start_urls.append("http://spiderbites.nytimes.com/free_" + str(x) + "/index.html")
	start_urls = ["http://spiderbites.nytimes.com/free_2014/index.html"]
	baseURL1 = "http://spiderbites.nytimes.com"
	baseURL2 = "http://www.nytimes.com/"

	def parse(self, response):
		for url in response.xpath('//div[@class="articlesMonth"]/ul/li/a/@href').extract():
			#self.log('@@@@ Got URL: %s' % (self.baseURL1+url))
			#yield scrapy.Request(self.baseURL1 + url.split("_")[-3] + "/" + url, callback = self.parseNews) #There are two kinds format exist,e.g. 2003
			yield scrapy.Request(self.baseURL1 + url, callback = self.parseNews)


	def parseNews(self, response):
		News = []
		News_urls = response.xpath('//ul[@id="headlines"]/li/a/@href').extract()
		News.extend([self.make_requests_from_url(url).replace(callback=self.parseSave) for url in News_urls])

		return News

	def parseSave(self, response):
		item = NYtimesItem()

		item["link"] = unicode(response.url)
		item["category"] = unicode(response.url.split("/")[-2])
		item["title"] = unicode(response.xpath('//meta[@name="hdl"]/@content').extract()[0])
		item["author"] = unicode(response.xpath('//meta[@name="byl"]/@content').extract()[0])
		item["date"] = unicode(response.xpath('//meta[@name="dat"]/@content').extract()[0])
		item["article"] = response.xpath('//p/text()').extract()

		yield item
