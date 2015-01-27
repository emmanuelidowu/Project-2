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
        print "Sorry wrong Password, You must exit now" + exit()
else:
    print "Sorry wrong username "+".You will have to exit now"
    exit()

FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"
response = urllib2.urlopen(FPurl).read()
data = json.loads(response)



def menu_FP_name():
    name_enter = raw_input("Please enter the company name you would like to export to csv:")
    count = 0
    with open('data2.csv','w+') as csvfile:
        fieldnames = ['Company Name', 'ID Number','Sector', 'Non Current Assets','Current Assets','Total Assets','Equity','Non Current Liabilities','Current Liabilities','Total Equity & Liabilities','Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data['rows']:
            FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']
            response2 = urllib2.urlopen(FPurl2).read()
            data2 = json.loads(response2)
            if 'sector' in data2:
                if data2['company']['name']== name_enter:
                    print data2['company']['name'], ' ID number....', data2['id']
                    writer.writerow({'Company Name':data2['company']['name'],'ID Number': data2['id'],'Sector':data2['sector'],'Non Current Assets': data2['company']['non_current_assets'],'Current Assets':data2['company']['current_assets'],'Total Assets':data2['company']['non_current_assets']+ data2['company']['current_assets'], 'Equity':data2['company']['equity'],'Non Current Liabilities':data2['company']['non_current_liabilities'],'Current Liabilities':data2['company']['current_liabilities'],'Total Equity & Liabilities':data2['company']['equity']+ data2['company']['non_current_liabilities']+ data2['company']['current_liabilities'],'Date':data2['date']})
                    count +=1
                    print "item number " , str(count) , " was written"
        print "All ", name_enter, " have been written to csv, please ensure you rename the csv file so that it doesnt get overwritten." 
    
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
    user_input=raw_input("Enter a sector that you would like to export to csv:")
    count = 0
    with open('sector_search.csv','w+')as csvfile:
        fieldnames = ['Company Name', 'ID Number','Sector', 'Non Current Assets','Current Assets','Total Assets','Equity','Non Current Liabilities','Current Liabilities','Total Equity & Liabilities','Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data['rows']:
            FPurl2 = "http://dev.c0l.in:5984/financial_positions/" + item['id']
            response2 = urllib2.urlopen(FPurl2).read()
            data2 = json.loads(response2)
            if 'sector' in data2:
                if data2['sector'] == user_input:
                    print data2['company']['name']," ID..",data2['id']
                    writer.writerow({'Company Name':data2['company']['name'],'ID Number': data2['id'],'Sector':data2['sector'],'Non Current Assets': data2['company']['non_current_assets'],'Current Assets':data2['company']['current_assets'],'Total Assets':data2['company']['non_current_assets']+ data2['company']['current_assets'], 'Equity':data2['company']['equity'],'Non Current Liabilities':data2['company']['non_current_liabilities'],'Current Liabilities':data2['company']['current_liabilities'],'Total Equity & Liabilities':data2['company']['equity']+ data2['company']['non_current_liabilities']+ data2['company']['current_liabilities'],'Date':data2['date']})
                    count +=1
                    print "item number ",str(count), " was written"
        print "All ", user_input, " have been written to csv, please ensure you rename the csv file so that it doesnt get overwritten."
        print "-------------------------"
                    
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
        if 'sector' in Idata2:
            if Idata2['sector'] == user_inputI:
                print Idata2['company']['name']," ID..",Idata2['id']
        #with open("data.csv",'wb')
    print"--------------------------"
    menu_FP() 

print "please select one of the following that you would like to view. (1 or 2)"
choice_1=raw_input("""1. Financial Position 
2. Income Statement
3. Search by name with the Financial Position data
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
