# main.py
# this file is for environment and connection setup
# also the UIs will be set up here too
# warning: this program only support simple txt file on url

import urllib.request
import xlwt
import time
import function

# test_url = https://www.google.com/finance/getprices?i=360&p=10d&f=d,o,h,l,c,v&df=cpct&q=AAPL

print (">> Welcome")

# data base init
db = function.db()

#asking for urls
db.ask_for_urls()

# workbook init
wb = xlwt.Workbook()
style0 = xlwt.easyxf('font: name Times New Roman',
    num_format_str='#,##0.00')

# time starts counting here
print(">>> running, please wait.")
start_time = time.time()

# a tab showing adding order
Tab = 0
count = 0
ws = wb.add_sheet("Order")
for url in db.urls:
	ws.write(count, 0, str(Tab), style0)
	ws.write(count, 1, url, style0)
	Tab += 1
	count += 1

Tab = 0
for url in db.urls: # get url
	# retrieving content from the websites (which are txt files)
	respond = urllib.request.urlopen(url)
	lines = respond.readlines() #whole txt

	ws = wb.add_sheet(str(Tab))
	count = 0
	for line in lines:
		ws.write(count, 0, line.decode("utf8"), style0)
		count += 1

	Tab += 1

# finishing up: file name editing && saving
current_time = time.localtime();
file_name = str(current_time.tm_year) + "_" + str(current_time.tm_mon) + "_"  + str(current_time.tm_mday) + "_" + str(current_time.tm_hour) + "_"  + str(current_time.tm_min) + "_"  + str(current_time.tm_sec) + ".xls"

wb.save(file_name)
respond.close()
print(">>> Done. Results are saved in %s. Please check program directory." % (file_name))
print(">>> Total time spent: %ss." % (time.time() - start_time))

