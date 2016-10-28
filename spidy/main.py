import threading 
# from multiprocessing import Queue
from Queue import Queue
from spider import Spider
from domain import *
from general import *



PROJECT_NAME = raw_input("Enter the project name: ")
HOMEPAGE = raw_input("Enter the url of the website:  ")
Type = raw_input("Enter type of file: ")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
DOWNLOADED_FILE = PROJECT_NAME + '/downloaded.txt'
NUMBER_OF_THREADS = 8
queue  = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME,Type)

def create_workers():
	for _ in xrange(NUMBER_OF_THREADS):
		t = threading.Thread(target = work)
		t.daemon = True
		t.start()

def work():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name,url)
		queue.task_done()

def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()


def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		print str(len(queued_links)) + 'links in the queue'
		create_jobs()

create_workers()
crawl()
