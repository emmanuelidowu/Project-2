import urllib2
import json

FPurl = "http://dev.c01.in:5984/financial_positions/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)

for item in data['rows']:
    print item['key']
