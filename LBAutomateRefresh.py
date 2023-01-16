from LBTracker import LBTracker
from random import randrange

import time

# Randomize the interval in which to check site
max_int = input("Enter a maximum time to check (seconds): ")
max_int = int(max_int)

# Hold current wine to compare if a new one is posted
current_wine = ''

while True:
	time.sleep(randrange(max_int))
	
	tracker = LBTracker()
	wine = tracker.get_wine()
	price = tracker.get_price()
	vintage = tracker.get_vintage()

	if wine != current_wine:
		current_wine = wine
		print(wine)
		print("\tPrice = $" + price)
		print("\tVintage = " + vintage)