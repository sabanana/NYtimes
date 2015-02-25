# -*- coding: utf-8 -*-

# Scrapy settings for NYtimes project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'NYtimes'

SPIDER_MODULES = ['NYtimes.spiders']
NEWSPIDER_MODULE = 'NYtimes.spiders'
ITEM_PIPELINES = {
	'NYtimes.pipelines.NYtimesPipeline' : 500,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'NYtimes (+http://www.yourdomain.com)'
