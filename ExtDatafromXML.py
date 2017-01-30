import urllib
import xml.etree.ElementTree as ET

sample_XML ='http://python-data.dr-chuck.net/comments_42.xml'
actual_XML = 'http://python-data.dr-chuck.net/comments_266069.xml'
url = actual_XML#sample_XML
uh = urllib.urlopen(url)
data = uh.read()
#print data
sum = 0
tree = ET.fromstring(data)
comments = tree.find('comments').findall('comment')

for comment in comments:
    thiscount = comment.find('count').text
    sum += int(thiscount)

print sum

