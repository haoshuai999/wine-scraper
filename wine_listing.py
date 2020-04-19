import lxml
import requests
import csv
import random
import pandas as pd
import re
from lxml.html import fromstring

def scrape(url):
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


	page_html_text = requests.get(url, headers=headers).text
	# try:
	# 	page_html_text = re.sub(r"<img class=\"(.*?)<\/noscript>", "", page_html_text)
	# except:
	# 	pass
	# print(page_html_text)
	page_html = fromstring(page_html_text)

	try:
		image = page_html.cssselect(".pipThumb-1 img")[0]
		image_url = "https://www.wine.com" + image.get('src')
		# print(image_url)
	except:
		image_url = ""
	
	try:
		name = page_html.cssselect(".pipName")[0]
		name_text = name.text_content().strip()
	except:
		name_text = ""

	if re.search(r"(.*)\b[1-9][0-9]{3}\b$", name_text):
		year_text = name_text[-5:].strip()
		name_text = name_text[:-5]
		# print(year_text)
		# print(name_text)
	else:
		year_text = ""

	try:
		genre = page_html.cssselect(".pipOrigin_link")[0]
		genre_text = genre.text_content()
	except:
		genre_text = ""

	try:
		place = page_html.cssselect(".pipOrigin_link")[1]
		place_text = place.text_content()
	except:
		place_text = ""
	# print(genre_text)
	# print(place_text)

	try:
		rating = page_html.cssselect(".averageRating_average")[0]
		rating_text = rating.text_content()
		# print(rating_text)
	except:
		rating_text = ""

	try:
		ratingnum = page_html.cssselect(".averageRating_number")[0]
		ratingnum_text = ratingnum.text_content()
		# print(ratingnum_text)
	except:
		ratingnum_text = ""

	try:
		capacity = page_html.cssselect(".prodAlcoholVolume")[0]
		capacity_text = capacity.text_content().replace("/", "").strip()
		# print(capacity_text)
	except:
		capacity_text = ""

	try:
		alcohol = page_html.cssselect(".prodAlcoholPercent_inner")[0]
		alcohol_text = alcohol.text_content().strip()
		# print(alcohol_text)
	except:
		alcohol_text = ""

	try:
		cp = page_html.cssselect(".productPrice_price-sale")[0]
		cp_text = cp.text_content().replace('\n','').strip()
		cp_text = re.sub(r' +', '.', cp_text)
		# print(cp_text)
	except:
		cp_text = ""


	try:
		op = page_html.cssselect(".productPrice_price-reg")[0]
		op_text = op.text_content().replace('\n','').strip()
		op_text = re.sub(r' +', '.', op_text)
		# print(op_text)
	except:
		op_text = ""

	try:
		ship = page_html.cssselect(".prodItemShipping")[0]
		ship_text = ship.text_content().replace('Ships ','').strip()
		# print(ship_text)
	except:
		ship_text = ""

	try:
		available = page_html.cssselect(".productUnavailable")[0]

		available_text = False
		# print(available_text)
	except:
		available_text = True
		# print(available_text)

	return (image_url, year_text, name_text, genre_text, place_text, rating_text, ratingnum_text, capacity_text, alcohol_text, op_text, cp_text, ship_text, available_text)

if __name__ == '__main__':
	# scrape("https://www.wine.com/product/world-tour-white-wine-collection/100295")
	f = open("wine_url.txt", "r")
	urls = f.readlines()
	urls = [("https://www.wine.com" + line.rstrip('\n')) for line in urls]
	url_list = []
	image_list = []
	year_list = []
	name_list = []
	genre_list = []
	place_list = []
	rating_list = []
	ratingnum_list = []
	capacity_list = []
	alcohol_list = []
	original_price_list = []
	current_price_list = []
	ship_list = []
	available_list = []

	count = 0
	for url in urls:
		# print(url)
		count += 1
		image, year, name, genre, place, rating, ratingnum, capacity, alcohol, original_price, current_price, ship, available = scrape(url)
		url_list.append(url)
		image_list.append(image)
		year_list.append(year)
		name_list.append(name)
		genre_list.append(genre)
		place_list.append(place)
		rating_list.append(rating)
		ratingnum_list.append(ratingnum)
		capacity_list.append(capacity)
		alcohol_list.append(alcohol)
		original_price_list.append(original_price)
		current_price_list.append(current_price)
		ship_list.append(ship)
		available_list.append(available)`
		if count % 500 == 0:
			print(count)
			print("output csv")
			df = pd.DataFrame(list(zip(url_list, image_list, year_list, name_list, genre_list, place_list, rating_list, ratingnum_list, capacity_list, alcohol_list, original_price_list, current_price_list, ship_list, available_list)),
				 columns=['listing_URL', 'image_URL', 'Year', 'Name', 'Genre', 'Place', 'Rating', 'Count_of_rating', 'Capacity', 'Alcohol_concentration', 'Original_Price', 'Current_price', 'Shipment', 'Available'])
			df.to_csv("wine_listing.csv", index=False, encoding='utf-8-sig')

	df = pd.DataFrame(list(zip(url_list, image_list, year_list, name_list, genre_list, place_list, rating_list, ratingnum_list, capacity_list, alcohol_list, original_price_list, current_price_list, ship_list, available_list)),
		 columns=['listing_URL', 'image_URL', 'Year', 'Name', 'Genre', 'Place', 'Rating', 'Count_of_rating', 'Capacity', 'Alcohol_concentration', 'Original_Price', 'Current_price', 'Shipment', 'Available'])
	df.to_csv("wine_listing.csv", index=False, encoding='utf-8-sig')