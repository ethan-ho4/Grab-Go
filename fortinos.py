from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
start_url = 'https://www.fortinos.ca/food/fruits-vegetables/c/28000?navid=flyout-L2-fruits-vegetables'
driver.get(start_url)
import time
time.sleep(20)
page_source = driver.page_source
print('product-name__item product-name__item--name' in page_source)

soup = BeautifulSoup(page_source , "lxml")
products = []
names_selector = soup.find_all('span' , class_ = 'product-name__item product-name__item--name')
prices_selector = soup.find_all('span' , class_ = 'price__value selling-price-list__item__price selling-price-list__item__price--now-price__value')
unit_prices_selector = soup.find_all('span' , class_= 'price__value comparison-price-list__item__price__value')
quants_selector = soup.find_all('span' , class_= 'price__unit comparison-price-list__item__price__unit')


for name_selector , price_selector , unit_price_selector , quant_selector in zip(names_selector , prices_selector , unit_prices_selector , quants_selector):
    listing = {
        "name" : name_selector.get_text().strip() , 
        "price" : price_selector.get_text().strip("$¢") ,
        "unit-price" : unit_price_selector.get_text().strip("$¢") ,
        "quantity" : quant_selector.get_text().strip("/") ,
    }
    products.append(listing)
print(len(products))

with open("fortinos.json" , "w") as fout:
    json.dump(products , fout , indent=4)