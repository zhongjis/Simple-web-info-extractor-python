# this file is for environment and connection setup
# also the UIs will be set up here too
# warning: this only works for txt file

import urllib.request

url = "https://www.google.com/finance/getprices?i=360&p=10d&f=d,o,h,l,c,v&df=cpct&q=AAPL"

respond = urllib.request.urlopen(url)
txt = respond.readlines()

count = 0

for i in txt:
	if count < 20:
		print(i.decode("utf8"))
		count += 1

respond.close()

