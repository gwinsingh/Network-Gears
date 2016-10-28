import os
import urllib2

def create_project_dir(directory):
	if not os.path.exists(directory):
		print "Creating project ",directory
		os.makedirs(directory)

# create_project_dir("thenewboston")
def create_data_files(project_name,base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	downloaded = project_name + '/downloaded.txt'
	if not os.path.isfile(queue):
		write_file(queue,base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,'')
	if not os.path.isfile(downloaded):
		write_file(downloaded,'')


def write_file(path,data):
	f = open(path,'w')
	f.write(data)
	f.close()

# create_data_files('thenewboston','https://thenewboston.com/')

def append_to_file(path,data):
	# data.encode('utf-8','ignore')
	with open(path,'a') as file:
		file.write(data+'\n')


def delete_file_contents(path):
	with open(path,'w'):
		pass

def file_to_set(filename):
	results = set()
	with open(filename,'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results

def set_to_file(links,file):
	delete_file_contents(file)
	for link in sorted(links):
		li = link.encode('utf-8','ignore')
		append_to_file(file,li)

def download_file(path,url):
	try:
		r = urllib2.urlopen(url)
		f = open(path+'/'+url.split('/')[-1].split('#')[0].split('?')[0],'w')
		f.write(r.read())
		f.close()
	except Exception,err:
		print Exception,err
	

