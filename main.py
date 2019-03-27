#!/usr/bin/env python3

__author__ = "David Poslt"
__credits__ = ["David Poslt"]
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "david.poslt@gmail.com"
__status__ = "Develop"

#import requests
from colored import fg, attr
from time import sleep
from sys import stdout


def credentials():
    allinone = ' Author: {author} \n Licence: {licence} \n Email: {email} \n Status: {status} \n'.format(author = __author__, licence = __license__, email = __email__, status = __status__)
    count = 0
    while len(allinone) != count:
       for i in str(allinone):
          count += 1
          stdout.write(i)
          stdout.flush()
          sleep(.300)

def seturl(url):
    return  url

#url = "https://confluence.moneta.cz"

def settingscollors():
    #set colors
    green = fg("green")
    red = fg("red")
    res = attr("reset")

    return green,red,res

def settimer():
    timer = 100
    count = 0

    return timer, count


def main():
    green, red, res = settingscollors()
    timer, count = settimer()
    url = seturl("https://confluence.moneta.cz")

    while count < timer:
        count +=1
        try:
            site = requests.get("https://confluence.moneta.cz")

            if str(site) == '<Response [200]>':
                stdout.write(f'Test: \r{count}: {green} Check ok {res}')
                stdout.flush()
                sleep(.700)
            else:
                print('Status isn\'t available')
        except:
            print(f'{red} connection aborted {res}')
            exit()


if __name__ == '__main__':
    main()