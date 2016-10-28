import os

# nmap -options -target server ip
def get_nmap(options, d_name):
    command = "nmap " + options + " " + d_name
    process = os.popen(command)
    results = str(process.read())
    return results
