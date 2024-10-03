import requests
import argparse
from time import sleep
import sys
import json
import os

BASE_URL = "https://crt.sh/?q={}&output=json&opt=excludeExpired"

   
parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -d google.com")
parser._optionals.title = "OPTIONS"
parser.add_argument('-d', '--domain', type=str, help='Specify Target Domain to get subdomains from crt.sh', required=True)
query =  parser.parse_args()
dname = query.domain
cname = 'common_name'

class FileHandle:
    ''' class for the file handling of the script. '''
    def __init__(self, fname, data) -> None:
        self.fname = fname
        self.data = data
    def write_file(fname, data):
        """write to file."""
        if not os.path.exists(dname):
            os.mkdir(dname)
        with open(f'{dname}/{fname}','w', encoding="utf-8") as file:
            file.write(data)
            file.close()


def get_data():
    ''' get json output from crt.sh and output to file named [domain]-output.json'''
    url_list=[]
    url = BASE_URL.format(str(dname))
    r = requests.get(url, timeout=25)
    response = r.json()
    output = json.dumps(response)
    FileHandle.write_file(fname=f'{dname}-output.json',data = output)
    for each in response:
        domain_name=each['common_name']
        url_list.append(domain_name)
    return url_list



def check_url():
    ''' function to check if urls respond, and if so get the data'''
    domain_list = get_data()
    count=0

    for d in domain_list:
        count +=1
        url = "http://"+d
        try:
            r = requests.get(url, timeout=25)
            sleep(.5)
            resp = r.status_code        
        except requests.exceptions.ConnectionError:
            pass
        if resp == 200:
            call_data= r.text
            FileHandle.write_file(d, call_data)
        else:
            FileHandle.write_file(d, str(resp))
    print(f"found [{count}]: urls, valable at /{dname}")

check_url()
