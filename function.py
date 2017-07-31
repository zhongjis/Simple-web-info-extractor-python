# function.py

class db:
	urls = []
	url = "default"

	def ask_for_urls(self):
		while self.url != "":
			self.url = input(">>> please input the url you want to use, or press enter to stop: ")
			if self.url != "":
				self.urls.append(self.url)
