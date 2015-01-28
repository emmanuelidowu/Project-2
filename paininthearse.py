import urllib
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

def menu_FP_name():
    FPurl = "http://dev.c0l.in:5984/financial_positions/_all_docs"
    response = urllib2.urlopen(FPurl).read()
    data = json.loads(response)
    name_enter = raw_input("Please enter the company name you would like to export to csv:")
    count = 0
    with open('name_search_FP.csv','w+') as csvfile:
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

        print "-------------------------"
        
                    
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
    with open('sector_search_FP.csv','w+')as csvfile:
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
    count = 0
    with open('sector_search_IS.csv','w+')as csvfile:
        fieldnames=['Company Name','ID Number','Sector','Sales','Opening Stock','Purchases','Closing Stock','Cost of Sales','Gross Profit','Expenses','Net Profit','Interest Payable','Interest Receivable','Profit for Period','Fiscal Year Beginning']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in dataI['rows']:
            ISurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id']
            Iresponse2 = urllib2.urlopen(ISurl2).read()
            Idata = json.loads(Iresponse2)
            if 'sector' in Idata:
                if Idata['sector'] == user_inputI:
                    print Idata['company']['name']," ID..",Idata['id']
                    writer.writerow({'Company Name':Idata['company']['name'],'ID Number':Idata['id'],'Sector':Idata['sector'],'Sales':Idata['company']['sales'],'Opening Stock':Idata['company']['opening_stock'],'Purchases':Idata['company']['purchases'],'Closing Stock':Idata['company']['closing_stock'],'Cost of Sales':Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock'],'Gross Profit':Idata['company']['sales']-(Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock']),'Expenses':Idata['company']['expenses'],'Net Profit':(Idata['company']['sales']-(Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock']))-Idata['company']['expenses'],'Interest Payable':Idata['company']['interest_payable'],'Interest Receivable':Idata['company']['interest_receivable'],'Profit for Period':(Idata['company']['sales']-(Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock']))-Idata['company']['interest_payable']+Idata['company']['interest_receivable'],'Fiscal Year Beginning':Idata['fiscal_year_beginning']})
                    count +=1
                    print "item number ",str(count), " was written"
        print "All ", user_input, " have been written to csv, please ensure you rename the csv file so that it doesnt get overwritten."
    print"--------------------------"


def menu_IS_name():
    ISurl = "http://dev.c0l.in:5984/income_statements/_all_docs"
    responseI = urllib2.urlopen(ISurl).read()
    dataI = json.loads(responseI)

    user_inputI=raw_input("Enter a company name that you would like to view:")
    count = 0
    with open('name_search_IS.csv','w+')as csvfile:
        fieldnames=['Company Name','ID Number','Sector','Sales','Opening Stock','Purchases','Closing Stock','Cost of Sales','Gross Profit','Expenses','Net Profit','Interest Payable','Interest Receivable','Profit for Period','Fiscal Year Beginning']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in dataI['rows']:
            ISurl2 = "http://dev.c0l.in:5984/income_statements/" + item['id']
            Iresponse2 = urllib2.urlopen(ISurl2).read()
            Idata = json.loads(Iresponse2)
            if 'sector' in Idata:
                if Idata['company']['name'] == user_inputI:
                    print Idata['company']['name']," ID..",Idata['id']
                    writer.writerow({'Company Name':Idata['company']['name'],'ID Number':Idata['id'],'Sector':Idata['sector'],'Sales':Idata['company']['sales'],'Opening Stock':Idata['company']['opening_stock'],'Purchases':Idata['company']['purchases'],'Closing Stock':Idata['company']['closing_stock'],'Cost of Sales':Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock'],'Gross Profit':Idata['company']['sales']-(Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock']),'Expenses':Idata['company']['expenses'],'Net Profit':(Idata['company']['sales']-(Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock']))-Idata['company']['expenses'],'Interest Payable':Idata['company']['interest_payable'],'Interest Receivable':Idata['company']['interest_receivable'],'Profit for Period':(Idata['company']['sales']-(Idata['company']['opening_stock']+Idata['company']['purchases']-Idata['company']['closing_stock']))-Idata['company']['interest_payable']+Idata['company']['interest_receivable'],'Fiscal Year Beginning':Idata['fiscal_year_beginning']})
                    count +=1
                    print "item number ",str(count), " was written"
        print "All ", user_inputI, " have been written to csv, please ensure you rename the csv file so that it doesnt get overwritten."
    print"--------------------------"



def sector_menu():
    print "please select one of the following that you would like to view. (1 or 2)"
    choice_1=raw_input("""1. Financial Position 
2. Income Statement:""")
    if choice_1 =="1":
        financial_positions()
    elif choice_1 =="2":
        income_statement()
    else:
        print "Sorry Incorrect number", sector_menu()

def name_search():
    print "Please select one of the following that you would like to view, or go back? (1 or 2)"
    choice_2=raw_input("""1. Financial Position 
2. Income Statement:""")
    if choice_2=="1":
        menu_FP_name()
    elif choice_2=="2":
        menu_IS_name()
    elif choice_2=="go back" or "Go Back" or "Go back":
        start_menu()
    else:
        print "Sorry Incorrect Number", name_search()

def start_menu():
    print "Would you like to search by name or sector?"
    choice_3=raw_input("Please enter your option:")
    if choice_3=="name" or "Name":
        name_search()
    elif choice_3=="sector" or "Sector":
        sector_menu()
    else:
        print "Sorry not an option, Goodbye"
        

start_menu()
print "We are done"
