# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class NYtimesPipeline(object):

	def __init__(self):
		self.titles_seen = set()

	def process_item(self, item, spider):
		filename = item["title"].replace('/','_').replace('\\','_').replace('.','_').replace('|','_') + ".txt"
		if filename in self.titles_seen:
			raise DropItem("Duplicate item found: %s" % filename)
		else:
			self.titles_seen.add(filename)
			with open('Download_Files/ %s' % filename, 'w+b') as f:
				f.write(item["link"] + '\n' + '\n' + item["category"] + '\n' + '\n' + item["title"] +'\n' + '\n' + item["author"] +'\n' + '\n' + item["date"] +'\n' + '\n' )
				for p in item["article"]:
					if p != None :
						f.write(p.encode('utf-8') + '\n')
