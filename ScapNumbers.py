import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')#
sampleurl = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_266072.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    sum += int(tag.contents[0])
    count += 1
print 'Count', count
print 'Sum', sum