# this file is for environment and connection setup
# also the UIs will be set up here too
# warning: this only works for txt file

import urllib.request
import xlwt
import time

print (">> Welcome")
# test_url = https://www.google.com/finance/getprices?i=360&p=10d&f=d,o,h,l,c,v&df=cpct&q=AAPL

url = "default"
urls = []

print(">> program runing")

while url != "":
	url = input(">> please input the url you want to use: ")
	if url != "":
		urls.append(url)

wb = xlwt.Workbook()
style0 = xlwt.easyxf('font: name Times New Roman',
    num_format_str='#,##0.00')

# time starts counting here
print(">> running, please wait.")
start_time = time.time()

Tab = 0
for i in urls: # get url
	# retrieving content from the websites (which are txt files)
	respond = urllib.request.urlopen(i)
	lines = respond.readlines() #whole txt

	ws = wb.add_sheet(str(Tab))
	count = 0
	for line in lines:
		ws.write(count, 0, line.decode("utf8"), style0)
		count += 1

	Tab += 1

# finishing up
wb.save('result.xls')
respond.close()
print(">> Done. result.xls saved. Please check program directory.")
print(">> Total time spent: %s s." % (time.time() - start_time))

