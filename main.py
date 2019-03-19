#!/usr/bin/env python3

__author__ = "David Poslt"
__credits__ = ["David Poslt"]
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "david.poslt@gmail.com"
__status__ = "Develop"

import requests, time
from colored import fg, attr

print(f' Author: {__author__} \n License: {__license__} \n version: {__version__} \n Email: {__email__} \n Status: {__status__} \n')

url = "https://your_url_adress"
timer = 1000 #count repeat
count = 0

#set colors
green = fg("green")
red = fg("red")
res = attr("reset")

while timer > 0:
    timer -=1
    count +=1
    try:
        site = requests.get(url)
        if str(site) == '<Response [200]>':
           print(f'Test {count}: {green} Check ok {res}')
            #request.session().close()
           time.sleep(.700)
        else:
            print('Status isn\'t available')
    except:
        print(f'{red}Connection aborted {res}')
        exit()

