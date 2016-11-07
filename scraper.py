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

from bs4 import BeautifulSoup
from urllib.request import urlopen

website = "https://www.racenet.com.au/horse-racing-results/"
rawSite = urlopen(website);
rawHTML = rawSite.read();
soup = BeautifulSoup(rawHTML, "html.parser")

locData = []


today = soup.find_all('div', attrs={"class":"grid_3 alpha"})
for tag in today:
	linkData = tag.find_all("a", {"class":"link_red"})
	for tag in linkData:
		if debug:
			print ("Location: ", tag.text)
			print ("Link: ", tag["href"], "\n")
		temp = {
			"loc": tag.text,
			"link": tag["href"]
		}
		locData.append(temp);
