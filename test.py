import re
import urllib
from BeautifulSoup import *
'''
s1 = "asdfag12"
s2="s1s2s3"
f1 = re.findall('[0-9]+',s1)
print f1
f2 = re.findall('[0-9]+',s2)
print f2,f2[1],dir(f2[1])#.properties()
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y
z = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
w= re.findall('\S+?@\S+',z)
print w

x = urllib.urlopen('http://www.py4inf.com/')
print x,'\n',type(x),'\n',dir(x),'\n',x.__doc__
'''
url = 'http://www.py4inf.com'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
x = soup('a')
for items in x:
    print items