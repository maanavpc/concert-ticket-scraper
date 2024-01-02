'''
Python webscraper for ticketmaster show prices
'''

import requests
from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup

# Variables
url = "https://www.vividseats.com/travis-scott-tickets-newark-prudential-center-11-24-2023--concerts-rap-hip-hop/production/4561100"
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

# Initializing a list with Useragents 
'''
useragentarray = [
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
]
'''


'''
def get(url, proxy):

	""" 
	Sends a GET request to the given url using given proxy server. 
	The proxy server is used without SSL, so the URL should be HTTP. 
 
	Args: 
		url - string: HTTP URL to send the GET request with proxy 
		proxy - string: proxy server in the form of {ip}:{port} to use while sending the request 
	Returns: 
		Response of the server if the request sent successfully. Returns `None` otherwise. 
 
	""" 
	try:
		r = requests.get(url, proxies={"http": f"http://{proxy}"}) 
		if r.status_code < 400: # client-side and server-side error codes are above 400 
			return r
		else: 
			print(r.status_code) 
	except Exception as e: 
		print(e) 
	return None
def check_proxy(proxy): 
	"""
	Checks the proxy server by sending a GET request to httpbin. 
	Returns False if there is an error from the `get` function 
	"""
	print("proxy is: " + str(proxy))
	print(get("http://httpbin.org/ip", proxy))
	return get("http://httpbin.org/ip", proxy) is not None
 '''


def initialize_Webdriver():
	# Create Chromeoptions instance
	options = webdriver.ChromeOptions()
	# Adding argument to enable fullscreen (me)
	options.add_argument("start-maximized");
	# Adding argument to disable the AutomationControlled flag
	options.add_argument("--disable-blink-features=AutomationControlled")
	# Exclude the collection of enable-automation switches
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	# Turn-off userAutomationExtension
	options.add_experimental_option("useAutomationExtension", False)
	# Setting the driver path and requesting a page
	driver = webdriver.Chrome(options=options)
	# Changing the property of the navigator value for webdriver to undefined
	driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

	return driver


def pullData(driver):
	seat_sections = []
	seat_sections = driver.find_elements_by_class_name("styles_listingRowContainer__3hXZy")
	print(seat_sections)

def main():
	#proxies = open("proxies.txt", "r").read().strip().split("\n")
	#available_proxies = list(filter(check_proxy, proxies))
	driver = initialize_Webdriver()

	'''
	for i in range(len(useragentarray)):
		# Setting user agent iteratively as Chrome 108 and 107 
		driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]})
		print(driver.execute_script("return navigator.userAgent;"))
		driver.get(url)
	'''
	driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragent})
	print(driver.execute_script("return navigator.userAgent;"))
	driver.get(url)

	pullData(driver)


	while True:
		time.sleep(1)



main()



'''
https://www.geeksforgeeks.org/python-web-scraping-tutorial/
https://github.com/maanavpc/concert-ticket-scraper

every time to run, do "source .venv/bin/activate"
'''