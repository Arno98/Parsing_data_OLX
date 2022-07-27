from bs4 import BeautifulSoup
import requests
from threading import Thread

page = requests.get('https://www.olx.ua/d/uk/zhivotnye/koshki/?currency=UAH')
bs = BeautifulSoup(page.text, 'html.parser')
ads = []

def images_ads():
	ads.append([img['src'] for img in bs.findAll("img")[:10]])

def titles_ads():
	ads.append([title.text for title in bs.findAll("h6")[:10]])
	
def prices_ads():
	ads.append([price.text for price in bs.findAll("p", attrs={"data-testid": "ad-price"})[:10]])

def ads_collection():
	t1 = Thread(target=images_ads())
	t2 = Thread(target=titles_ads())
	t3 = Thread(target=prices_ads())
	
	t1.start()
	t2.start()
	t3.start()
	
	t1.join()
	t2.join()
	t3.join()
	
	return ads
