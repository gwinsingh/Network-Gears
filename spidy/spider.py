from bs4 import BeautifulSoup
import urllib2

from urllib2 import urlopen
from link_finder import LinkFinder
from general import *

class Spider:
	"""docstring for Spider"""

	projectname = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	Type=''
	download_file = ''
	downloaded = set()
	queue = set()
	crawled = set()


	def __init__(self,projectname,base_url,domain_name,Type):
		# self.arg = argc
		Spider.projectname = projectname
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.projectname + '/queue.txt'
		Spider.crawled_file = Spider.projectname + '/crawled.txt'
		Spider.download_file = Spider.projectname + '/downloaded.txt'
		Spider.Type = Type

		self.boot()
		self.crawl_page('First Spider',Spider.base_url)

	@staticmethod
	def boot():
		create_project_dir(Spider.projectname)
		create_data_files(Spider.projectname,Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)	
		Spider.downloaded = file_to_set(Spider.download_file)

	@staticmethod
	def crawl_page(thread_name,page_url):
		if page_url not in Spider.crawled:
			print thread_name,'crawling',page_url
			print('Queue '+str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			# if Spider.Type == "image":
			# 	Spider.get_images(page_url)
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()


	@staticmethod
	def gather_links(page_url):
		html_string = ''
		try:
			request = urllib2.Request(page_url)
			response = urllib2.urlopen(request)
			# response = urllib2.urlopen(page_url)
			u = response.info().getheader('Content-Type')
			print u
			# print Spider.Type
			

			if u.find(Spider.Type) != -1:	
				vv = page_url		
				if vv not in Spider.downloaded:
					download_file('./'+Spider.projectname,vv)
					Spider.downloaded.add(vv)

			if u.startswith('text/html'):
				if Spider.Type == "image":
					Spider.get_images(page_url)
				html_bytes = response.read()
				html_string = html_bytes.decode('utf-8')

				# print "here"
			
			finder = LinkFinder(Spider.base_url,page_url)
			finder.feed(html_string)
		except Exception,err:
			# print('Error: cannot crawl page')
			print Exception,err
			return set()
		return finder.page_links()

	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def update_files():
		set_to_file(Spider.queue,Spider.queue_file)
		set_to_file(Spider.crawled,Spider.crawled_file)
		set_to_file(Spider.downloaded,Spider.download_file)

	@staticmethod
	def get_images(page_url):
		html = urllib2.urlopen(page_url)
		# soup = BeautifulSoup(page_url)

		soup = BeautifulSoup(html)
		print "more in"
					# soup.prettify()
					# print soup.prettify()
		for tag in soup.findAll("img"):
						# print tag.get('src')
			if tag.get('src') not in Spider.downloaded:
				download_file('./'+Spider.projectname,tag["src"])
				Spider.downloaded.add(tag["src"])