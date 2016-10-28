import urlparse

def get_sub_domain_name(url):
	try:

		# print urlparse(url)
		return urlparse.urlparse(url).netloc
	except:
		return ''

def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2]+'.'+results[-1]
	except:
		return ''

# print get_domain_name("http://stackoverflow.com/questions/31601238/python-2-7-10-error-from-urllib-request-import-urlopen-no-module-named-request")