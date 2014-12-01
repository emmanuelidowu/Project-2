def BirminghamCity():
    print "Gonna win the league"
BirminghamCity()
BirminghamCity()
aList ={'Blues':"Midlands Number One",'Villa':"Awful Team"}
choice = raw_input('Who are the best team in Birmingham? Blues or Villa?')
if choice == 'Blues':
    print aList['Blues']
    BirminghamCity()
elif choice == 'Villa':
    print aList['Villa']
else:
    print 'Dont Be Silly' 
