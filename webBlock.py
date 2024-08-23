
import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

web_list = [
    "www.facebook.com",
    "facebook.com",
]

def block_web(web_list):
    print("running", web_list)
    with open(hosts_path, 'a') as hosts_file:
        for website in web_list:
            hosts_file.write('127.0.0.1 '+website+'\n')
        
def unblock_web(web_list):
    print("unblock")
    with open(hosts_path, 'r+') as hosts_file:
        lines = hosts_file.readlines()
        hosts_file.seek(0)
        for line in lines:
            if not any(website in line for website in web_list):
                hosts_file.write(line)
        hosts_file.truncate()
        

block_web(web_list)

# unblock_web(web_list)