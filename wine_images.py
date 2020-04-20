import pandas as pd
import numpy as np
import requests
import shutil
import sys

df = pd.read_csv("wine_listing.csv")
# print(df["image_URL"])

all_urls = df["image_URL"]

start_url = int(sys.argv[1].lower())

for i in range(start_url - 1, len(all_urls)):
	if (i+1) % 5000 == 0:
		print(i + 1)
	if type(all_urls[i]) == float:
		continue
	response = requests.get(all_urls[i], stream=True)
	with open('images/img'+ str(i+1) + '.jpg', 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response