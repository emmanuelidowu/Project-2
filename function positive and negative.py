#Taking the name and opinion as arguments
number = int(raw_input('Enter a number:'))
def PosNeg(number):
    if number >0:
        print 'Positive'
    elif number <0:
        print 'Negative'
PosNeg(number)

#Exercise2

FirstTeam = raw_input('Enter a football team')
SecondTeam = raw_input('Enter another football team')

def LenCompare():

    FirstTeamLen = int(len(FirstTeam))
    SecondTeamLen = int(len(SecondTeam))

    if FirstTeamLen > SecondTeamLen:
        print FirstTeam
    elif FirstTeamLen == SecondTeamLen:
        print ('Same Length')
    else:
        print SecondTeam

LenCompare()

    
