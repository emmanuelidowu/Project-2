import urllib2
import json
import csv

name = raw_input("Whats your username? ")
if name == 'admin':
    print ("Hello "+name)
    pwd = raw_input("What is your password? ")
    if pwd == 'password':
        print "Please continue"
    else:
        print "Sorry wrong Password"
else:
    print "Sorry wrong username"

FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)

user_input=raw_input("Enter a sector:")

counter = 0

for item in data['rows']:
    FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']
    response2 = urllib2.urlopen(FPurl2).read()
    data2 = json.loads(response2)

    if data2['sector'] == user_input:
        print data2['company']['name']
             
        

print "We are done"
    #if user_input == "healthcare":
        #print data2['sector']=="healthcare"
