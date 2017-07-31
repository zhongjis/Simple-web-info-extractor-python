# function.py
import urllib.request
import time
import xlwt

class db:
	urls = []
	url = "default"

	def ask_for_urls(self):
		while self.url != "":
			self.url = input(">>> please input the url you want to use, or press enter to stop: ")
			if self.url != "":
				self.urls.append(self.url)

class workbook:
	wb = xlwt.Workbook()

	# add an intro page showing the adding history incase user need it
	def add_intro(self, urls, style):
		tab = 0
		count = 0
		ws = self.wb.add_sheet("Intro")

		for url in urls:
			ws.write(count, 0, str(tab), style)
			ws.write(count, 1, url, style)
			tab += 1
			count += 1

	# add pages for each url
	def add_sheets(self, urls, style):
		tab = 0

		for url in urls:
			respond = urllib.request.urlopen(url)
			lines = respond.readlines()

			count = 0
			ws = self.wb.add_sheet(str(tab))
			for line in lines:
				ws.write(count, 0, line.decode("utf8"), style)
				count += 1
			tab += 1
		respond.close()

	def save(self, file_name):
		self.wb.save(file_name)

