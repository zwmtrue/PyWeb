import json
import urllib


sample_Json = 'http://python-data.dr-chuck.net/comments_42.json'
actual_Json = 'http://python-data.dr-chuck.net/comments_266073.json'
uh = urllib.urlopen(actual_Json)
data = uh.read()
info = json.loads(data)
print 'User count:', len(info['comments'])
sum = 0
for item in info['comments']:
    sum += item['count']

print sum