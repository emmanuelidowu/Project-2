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
    print "Sorry wrong username "+".You will have to exit now"
    exit()

FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)



def menu_FP_name():
    count = 0
    name_enter = raw_input("Please enter the company name you would like")
    for item in data['rows']:
        FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']
        response2 = urllib2.urlopen(FPurl2).read()
        data2 = json.loads(response2)
        if data2['company']['name']== name_enter:
            count+=1
            fieldnames = ['Company Name', 'Non Current Assets','Current Assets','Total Assets']
            csvfile1=open('dataa.csv',"wb")
            datacsv.writerow({'Company Name': data2['company']['name'],
                             'Non Current Assets': data2['company']['non_current_assets'],
                             'Current Assets':data2['company']['current_assets'],
                             'Total Assets':data2['company']['non_current_assets']+data2['company']['current_assets']})
            print count
    
        

def menu_FP():
    choice_FP = raw_input("""Please select one of the following the view it:
1.Company Name
2.Company Sector
3.Non current assets
4.Current assests
5.Total assets
6.Equity
7.Non current liabilities
8.Current liabilities
9.Total Equity & Liabilities""")


    if choice_FP == "1" or "Company Name" or "Name":
        print data2['company']['name']
    
    
def financial_positions():

    FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"
    response = urllib2.urlopen(FPurl).read()
    data = json.loads(response)

    print """Different sectors:
'utilities,'
'consumer goods,'
'healthcare,'
'basic materials,'
'services,'
'technology,'
'industry goods,'
'financial'"""
    user_input=raw_input("Enter a sector that you would like to view:")

    for item in data['rows']:
        FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']
        response2 = urllib2.urlopen(FPurl2).read()
        data2 = json.loads(response2)
        if data2['sector'] == user_input:
            print data2['company']['name']," ID..",data2['id']

            
def income_statement():
    ISurl = "http://dev.c0l.in:5984/income_statements/_all_docs"
    responseI = urllib2.urlopen(ISurl).read()
    dataI = json.loads(responseI)

    print """Different sectors:
'utilities,'
'consumer goods,'
'healthcare,'
'basic materials,'
'services,'
'technology,'
'industry goods,'
'financial'"""
    user_inputI=raw_input("Enter a sector that you would like to view:")

    for item in dataI['rows']:
        ISurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id']
        Iresponse2 = urllib2.urlopen(ISurl2).read()
        Idata2 = json.loads(Iresponse2)
        if Idata2['sector'] == user_inputI:
            print Idata2['company']['name']," ID..",Idata2['id']
    print "Okay there are the companies, what would you like to do next"
            
            

    

print "please select one of the following that you would like to view. (1 or 2)"
choice_1=raw_input("""1. Financial Position 
2. Income Statement
""")
if choice_1 =="1":
    financial_positions()
elif choice_1 =="2":
    income_statement()
elif choice_1=="3":
    menu_FP_name()
else:
    print "Sorry Incorrect number"

print "We are done"
    #if user_input == "healthcare":
        #print data2['sector']=="healthcare"
