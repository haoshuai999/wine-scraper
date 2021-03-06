import lxml
import requests
import random
import sys
from lxml.html import fromstring

def scrape(urls, article_urls):
	user_agent_list = [
		"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
		"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
		"Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
		"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML, likeGecko)Chrome / 17.0.963.56Safari / 535.11",
		"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
		"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
	]


	headers = {
		'User-Agent': random.choice(user_agent_list)
	}

	page_html_text = requests.get(urls, headers=headers).text
	page_html = fromstring(page_html_text)
	links = page_html.cssselect(".prodItemInfo_link")
	for link in links:
		article_urls.append(link.get('href'))

	return article_urls

if __name__ == '__main__':
	start_page = int(sys.argv[1].lower())
	article_urls = []
	for i in range(start_page - 1, 15612):
		urls = "https://www.wine.com/list/wine/7155/" +  str(i + 1) + "?showOutOfStock=true"
		scrape(urls, article_urls)
		if (i + 1) % 500 == 0:
			print("scaping page %d" % (i + 1))
			with open('wine_url_'+ str(start_page) + '_' + str(i + 1) +'txt', 'w') as f:
				for item in article_urls:
					f.write("%s\n" % item)

	with open('wine_url_'+ str(start_page) + '_end.txt', 'w') as f:
		for item in article_urls:
			f.write("%s\n" % item)