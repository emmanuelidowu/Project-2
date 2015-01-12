import urllib2
import json



FPurl="http://dev.c0l.in:5984/financial_positions/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)
print data

ISurl="http://dev.c0l.in:5984/income_statements/_all_docs"
response = urllib2.urlopen(ISurl).read()
data = json.loads(response)
print data 
