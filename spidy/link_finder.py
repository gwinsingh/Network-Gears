from HTMLParser import HTMLParser
import urlparse

class LinkFinder(HTMLParser):
	# """docstring for LinkFinder"""
	def __init__(self,base_url,page_url):
		HTMLParser.__init__(self)
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()
		
	
	def handle_starttag(self,tag,attrs):
		if tag == 'a':
			for (attribute,value) in attrs:
				if attribute == 'href':
					url = urlparse.urljoin(self.base_url,value)
					self.links.add(url)

	

	def page_links(self):
		return self.links

	def error(self,message):
		pass

# finder = LinkFinder()
# finder.feed('<html><head><title>Test</title></head>'
# 	'<body><h1>Parse Me</h1></body></html>')
