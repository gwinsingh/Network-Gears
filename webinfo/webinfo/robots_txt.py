import urllib2
import io
import requests

def get_robots_txt(url):
    if url.endswith('/'):
        path=url
    else:
        path=url+'/'
    r = urllib2.urlopen(path+'robots.txt')
    return r.read()
    


# def get_robots_txt(url):
#     if url.endswith('/'):
#         path = url
#     else:
#         path = url + '/'
#     req = urllib.request.urlopen(path + 'robots.txt', data=None)
#     data = io.TextIOWrapper(req, encoding='utf-8')
#     return data.read()