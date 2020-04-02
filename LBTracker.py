from bs4 import BeautifulSoup

import requests

class LBTracker():

	def __init__(self):
		self.url = 'https://www.lastbottlewines.com'
		self.wine = ''
		self.price = ''

	def __str__(self):
		return "LastBottleWines.com tracker."

	def get_wine(self):
		self.parse_soup()
		return self.wine

	def get_price(self):
		self.parse_soup()
		return self.price

	def get_soup(self):
		source = requests.get(self.url).text
		soup = BeautifulSoup(source, 'lxml')
		return soup

	def parse_soup(self):
		soup = self.get_soup()
		self.wine = soup.find('h1', {'class': 'offer-name'}).text.strip()
		self.price = soup.find('span', {'class': 'amount lb'}).text.strip()
