import urllib, urllib2
import json
import time

params = urllib.urlencode({'board_id':'board_alumni99','page':100})
s = time.time()
f = urllib2.urlopen("http://api.caucse.net/gochiapi/articles/list?%s" % params)
e = time.time()
print e-s,"s"

obj = f.read()
obj = json.loads(obj)
print obj['option']
raw_input()
ret = json.dumps(obj, ensure_ascii=False, indent=2)

print ret
