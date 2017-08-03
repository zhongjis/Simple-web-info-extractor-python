# main.py
# this file is for environment and connection setup
# also the UIs will be set up here too
# warning: this program only support simple txt file on url

import time
import xlwt
import function

# test_url = https://www.google.com/finance/
# getprices?i=360&p=10d&f=d,o,h,l,c,v&df=cpct&q=AAPL

print(">>> Welcome")

# data base init
db = function.db()
db.ask_for_urls()

if db.urls == []:
    print(">>> Quiting...")
else:
    # workbook init
    result_doc = function.workbook()
    style0 = xlwt.easyxf(
        "font: name Times New Roman",
        num_format_str="#,##0.00")  # default style

    print(">>> running, please wait.")
    # time starts counting here
    start_time = time.time()
    result_doc.add_intro(db.urls, style0)
    result_doc.add_sheets(db.urls, style0)

    # finishing up: file name editing && saving
    current_time = time.localtime()
    file_name = str(current_time.tm_year) + \
        "_" + str(current_time.tm_mon) + \
        "_" + str(current_time.tm_mday) + \
        "_" + str(current_time.tm_hour) + \
        "_" + str(current_time.tm_min) + \
        "_" + str(current_time.tm_sec) + ".xls"

    result_doc.save(file_name)
    print(""">>> Done. Results are saved in %s. """ % (file_name) +
          """Please check program directory.""")
    print(">>> Total time spent: %ss." % (time.time() - start_time))
