# -*- coding: utf-8 -*-

# Scrapy settings for arbitrage_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os, sys
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DJANGO_BASE_DIR = os.path.join(PROJECT_DIR, 'arbitrage_web')
sys.path.insert(0, DJANGO_BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'arbitrage_web.settings'

BOT_NAME = 'arbitrage_scraper'

SPIDER_MODULES = ['arbitrage_scraper.spiders']
NEWSPIDER_MODULE = 'arbitrage_scraper.spiders'
ITEM_PIPELINES = ['arbitrage_scraper.pipelines.MegabetScraperPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'arbitrage_scraper (+http://www.yourdomain.com)'
