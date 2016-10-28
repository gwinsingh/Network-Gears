# tld extracts top level domain from the URL given
from tld import get_tld

# returns the top level domain name of the url
def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name


