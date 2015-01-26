import urllib2
import json

FPurl="http://dev.c0l.in:5984/financial_positions/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)

sector = raw_input("Please input a sector: ")

for item in data['rows']['sector']:
    print item
    



    





