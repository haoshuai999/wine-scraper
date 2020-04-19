# Scrape data from wine.com

The script in the repo is used to scrape information about wine from [wine.com](https://www.wine.com/).

- The "wine\_url.py" file is used to scrape a list of URLs.
- The "wine\_listing.py" file is used to scrape each listing of wine.
- The "wine\_image.py" file is used to download images of wine.

## To scrape the data about wine listings, please:
1. Install [Python3.6.9](https://www.python.org/downloads/) on your laptop or computer
2. Download the script "wine\_url.py", "wine\_listing.py", "wine\_image.py" and requirements.txt
3. In the same directory, Run the following command:
	
	Install required Python libraries
```sh
$ pip install -r requirements.txt
``` 
	
	This command will generate a "wine\_url.txt" file in the same directory which will be used in the next step
```sh
$ python wine_url.py
```
	
	This command will generate a "wine\_listing.csv" file containing all information about each type of wine. The CSV file will be used in the next step
```sh
$ python wine_listing.py
```
	
	This command will download all the related thumbnail images of the wine listings. For example, img1.jpg is the thumbnail image for the first listing
```sh
$ python wine_image.py
```