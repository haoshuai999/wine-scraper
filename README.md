# Scrape data from wine.com

The script in the repo is used to scrape information about wine from [wine.com](https://www.wine.com/).

- The "wine\_url.py" file is used to scrape a list of URLs.
- The "wine\_listing.py" file is used to scrape each listing of wine.
- The "wine\_image.py" file is used to download images of wine.

## To scrape the data about wine listings, please:
1. **Install [Python3.6.9](https://www.python.org/downloads/) on your laptop or computer**
2. **Download the script "wine\_url.py", "wine\_listing.py", "wine\_image.py" and requirements.txt**
3. **Install required Python libraries by running:**
```sh
$ pip install -r requirements.txt
```
4. **Scrape all the urls by running:**
```sh
$ python wine_url.py [start_page_number]
```
- Replace the [start_page_number] variable with 0 if you start from scratch, or replace with the page number you want to start with. 
- A larger TXT file named "wine\_url\_[start_page_number]\_[end_page_number].txt" will be generated every time the script scrapes 5000 items. 
- The command will finally generate a "wine\_url\_[start_page_number]\_end.txt" file in the same directory.
- Combine all the TXT files and name it as wine\_url.txt," so that it can be used in the next step.
- Delete redundant TXT files after the task finishes.

5. **Scrape all the wine by running:**
```sh
$ python wine_listing.py [start_url_number]
```
- Replace the [start_url_number] variable with 0 if you start from scratch, or replace with the URL number you want to start with. 
- A larger CSV file named "wine\_listing\_[start_url_number]\_[end_url_number].csv" will be generated every time the script scrapes 5000 items. 
- The command will finally generate a "wine\_listing\_[start_url_number]\_end.csv" file in the same directory.
- Combine all the CSV files and name it as wine\_listing.csv," so that it can be used in the next step.
- Delete redundant CSV files after the task finishes.

6. **Download all thunbnail images by running:**
```sh
$ python wine_image.py [start_url_number]
```
- Create a folder named "images" in the same directory.
- Replace the [start_url_number] variable with 0 if you start from scratch, or replace with the URL number you want to start with.
- A number will be printed to the command line every time the script download 5000 images. 
- The command will download all the related thumbnail images of the wine listings. For example, img1.jpg is the thumbnail image for the first listing.