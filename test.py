from sys import stdout
from time import sleep

__author__ = "David Poslt"
__credits__ = ["David Poslt"]
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "david.poslt@gmail.com"
__status__ = "Develop"

count = 0


allinone = ' Author: {author} \n Licence: {licence} \n Email: {email} \n Status: {status} \n'.format(author = __author__, licence = __license__, email = __email__, status = __status__)

while len(allinone) != count:
   for i in str(allinone):
      count += 1
      stdout.write(i)
      stdout.flush()
      sleep(.300)


