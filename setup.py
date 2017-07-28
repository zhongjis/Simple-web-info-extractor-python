# this file is for environment and connection setup
# also the UIs will be set up here too
# warning: this only works for txt file

import urllib.request
import xlwt



url = "https://www.google.com/finance/getprices?i=360&p=10d&f=d,o,h,l,c,v&df=cpct&q=AAPL"

# retrieving content from the websites (which are txt files)
respond = urllib.request.urlopen(url)
txt = respond.readlines()

# adding lines to excel file 
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
style0 = xlwt.easyxf('font: name Times New Roman',
    num_format_str='#,##0.00')

count = 0;

for i in txt:
		ws.write(count, 0, i.decode("utf8"), style0)
		count += 1

wb.save('test.xls')

respond.close()

