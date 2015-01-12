import urllib2
import json

FPurl="http://dev.c0l.in:5984/financial_positions/"
response = urllib2.urlopen(FPurl).read()
#id= int(['rows']['id'])

#abc=raw_input("enter company id")
for rows in FPurl:
    name = int(raw_input(rows["key"]))
    print name
    
