import pandas as pd
import numpy as np
import requests
import shutil

df = pd.read_csv("wine_listing.csv")
# print(df["image_URL"])

all_urls = df["image_URL"]
for i in range(len(all_urls)):
	if type(all_urls[i]) == float:
		continue
	response = requests.get(all_urls[i], stream=True)
	with open('images/img'+ str(i+1) + '.jpg', 'wb') as out_file:
	    shutil.copyfileobj(response.raw, out_file)
	del response