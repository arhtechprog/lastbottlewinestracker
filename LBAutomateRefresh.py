from LBTracker import LBTracker

import time

refresh_rate = input("Enter a refresh frequency (seconds): ")
refresh_rate = int(refresh_rate)

while True:
	time.sleep(refresh_rate)
	tracker = LBTracker()
	wine = tracker.get_wine()
	price = tracker.get_price()
	print(wine + " - $" + price)