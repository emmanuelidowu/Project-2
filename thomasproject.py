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
    counter = 0
    #first we should open the file and prepare it for writing
    with open('companies.csv', 'w+') as csvfile:
        fieldnames = ['Company Name', 'Equity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        #now as file is ready we should iterate through data to check which row we want to write to the file
        for item in data['rows']:
            FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']
            response2 = urllib2.urlopen(FPurl2).read()
            data2 = json.loads(response2)
            if data2['sector'] == user_input:
                print data2['company']['name']," ID..",data2['id']
                #once we find a row that matches our criteria we write it to the file
                writer.writerow({'Company Name': data2['company']['name'], 'Equity': data2['company']['equity']})
                counter += 1
    print "item number " + str(counter) + " was written"
 
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
else:
    print "Sorry Incorrect number"
 
print "We are done"
    #if user_input == "healthcare":
        #print data2['sector']=="healthcare"
 
