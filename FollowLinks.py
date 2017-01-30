import urllib
from BeautifulSoup import *

#count =int(raw_input('Enter Count:'))
#position = int(raw_input('Enter Position:'))-1
count =7
position =18-1
start_url_sample = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
start_url = 'http://python-data.dr-chuck.net/known_by_Caitlyn.html '
url = start_url#start_url_sample#
print 'Retriving:',url
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup('a')
lastnames=[]
lastnames.append(re.findall('known_by_([A-Za-z]+)\.html', url))

trips = 0
while trips < count:
    trips += 1
    url = tags[position].get('href', None)
    lastnames.append(re.findall('known_by_([A-Za-z]+)\.html', str(url)))
    print 'Retriving:',url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')

print 'The answer to the assignment for this execution is"',lastnames[count][0],'"'


