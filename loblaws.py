from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
start_url = 'https://www.loblaws.ca/food/fruits-vegetables/c/28000?navid=flyout-L2-fruits-vegetables'
driver.get(start_url)
import time
time.sleep(20)
print('product-name__item product-name__item--name' in driver.page_source.encode('utf-8').decode('utf-8'))