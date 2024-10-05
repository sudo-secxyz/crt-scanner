import re
import requests
import sys

class get_headers():


    def scan_it(target):
        results = []
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        urls = target
        for url in urls:
            url = url.strip()
            url = f"https://{url}"
            print(f'+ gathering header data for {url}')
            try:
                req = requests.get(url, headers=headers)
            except:
                message = 'no data'
                return message

            #print (url, 'report:')
            
            try:
                protection_xss = req.headers['X-XSS-Protection']
                if protection_xss != '1; mode=block':
                    p1 = 'X-XSS-Protection not set properly, XSS May be Possible:', protection_xss
    
                else:
                    p1 = 'X-XSS-Protection set, Congrats!'
                    
            except KeyError:
                p1 = 'X-XSS-Protection not set, XSS May be Possible: ' 
                
            try:
                options_content_type = req.headers['X-Content-Type-Options']
                if options_content_type != 'nosniff':
                    p2 = 'X-Content-Type-Options not set properly:'
                    
                else:
                    p2 = 'X-Content-Type-Options  set: Congrats!'
                
            except KeyError:
                p2 = 'X-Content-Type-Options not set'
                
            try:
                transport_security = req.headers['Strict-Transport-Security']
                if transport_security != '': 
            
                    p3 = 'Strict Transport in place', transport_security
                    
                else:
                    p3 = 'HSTS header not set properly, Man in the middle attacks is possible'
                    
                
            except KeyError:
                p3 = 'HSTS header not set properly, Man in the middle attacks is possible'
                

            try:
                content_security = req.headers['Content-Security-Policy']
                if content_security != '':

                    p4 = 'Content-Security-Policy set:', content_security
                    
                else:
                    p4 = 'Content-Security-Policy missing'
                    
            except KeyError:
               p4 = 'Content-Security-Policy missing'

        results = {
                    "protection_xss": p1,
                    "options_content_type": p2,
                    "transport_security": p3,
                    "content_security": p4
                    }
        return results

