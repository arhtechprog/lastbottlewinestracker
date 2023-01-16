from bs4 import BeautifulSoup

import re
import requests

LB_URL = 'https://www.lastbottlewines.com'
LB_OFFER_NAME_TAG = 'offer-name'
LB_PRICE_TAG = 'amount lb'

class LBTracker():

	def __init__(self):
		self.url = LB_URL
		self.wine = ''
		self.price = ''
		self.year = ''

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
		soup = BeautifulSoup(source, features="html.parser")
		return soup

	def parse_soup(self):
		soup = self.get_soup()
		self.wine = soup.find('h1', {'class': LB_OFFER_NAME_TAG}).text.strip()
		self.price = soup.find('span', {'class': LB_PRICE_TAG}).text.strip()

	# parse vintage year from wine name
	def get_vintage(self):

		# find "20" or "19" as start of vintage years
		match = re.search("20|19", self.wine)

		if match is not None:
			start = match.span()[0]

			# assume full year is listed
			end = start + 4
			self.year = self.wine[start:end]

		return self.year

