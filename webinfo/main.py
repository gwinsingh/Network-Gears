from webinfo import *
import os


ROOT_DIR = 'companies'

# from general.py
general.create_dir(ROOT_DIR)


def gather_info(name, url):
    print("\nGathering info")
    d_name = domain_name.get_domain_name(url)
    ip_addr = ip_address.get_ip_address(d_name)
    n_map = nmap.get_nmap("-F", d_name)
    r_txt = robots_txt.get_robots_txt(url)
    w_is = whois.get_whois(d_name)
    create_report(name, url, ip_addr, d_name, n_map, r_txt, w_is)


def create_report(name, full_url, ip_address, domain_name, nmap, robots_txt, whois):
    print("Creating report")
    project_dir = ROOT_DIR + '/' + name
    # get_robots_txt(project_dir,full_url)
    general.create_dir(project_dir)
    general.write_file(project_dir + '/full_url.txt', full_url)
    general.write_file(project_dir + '/domain_name.txt', domain_name)
    general.write_file(project_dir + '/ipaddress.txt', ip_address)
    general.write_file(project_dir + '/nmap.txt', nmap)
    general.write_file(project_dir + '/robots.txt', robots_txt)
    general.write_file(project_dir + '/whois.txt', whois)

def download_file(path,url):
    try:
        r = urllib2.urlopen(url)
        f = open(path+'/'+url.split('/')[-1].split('#')[0].split('?')[0],'w')
        f.write(r.read())
        f.close()
    except Exception,err:
        print Exception,err

print "Enter the Project Name:"
inp = str(raw_input())
print "Enter the URL:"
inp2 = str(raw_input())
gather_info(inp, inp2)

print "\n##\tThe report has created in the folder ./webinfo/"+inp+"/\n\n"