# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import scrapy

class RacingItem(scrapy.Item):
    fin = scrapy.Field()
    runner = scrapy.Field()
    odds = scrapy.Field()


class RacingSpider(scrapy.Spider):
    name = 'racenet.com.au'
    allowed_domains = ['racenet.com.au']
    start_urls = ['https://www.racenet.com.au/horse-racing-results/']
    
    def parse(self, response):
    	for table in response.xpath('.//table[@class="tblLatestHorseResults"]'):
		    rows = table.xpath('.//tr[@class="tr_res_runner"]')
		    for row in rows:
		        item = RacingItem()
		        item['fin'] = row.xpath('.//td[@class="first"]/text()').extract()
		        item['runner'] = row.xpath('.//td[2]/a[@class="link_red bold"]/text()').extract()
		        item['odds'] = row.xpath('.//td[@class="res_odds sb res_td_light last"]/span/text()').extract()
		        yield item
