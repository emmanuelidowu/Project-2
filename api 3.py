code=raw_input("Enter a company code")

import urllib
import json

url = "http://dev.c0l.in:8888/"

response = urllib.urlopen(url+code).read()
data = json.loads(response)
print data
