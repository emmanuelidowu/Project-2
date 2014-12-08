entry = raw_input("Would you like to see wage or name? ")

class Employee:
    def __init__(self):
        self.name="Dom"
        self.wage="30000 Pounds"

myEmployee = Employee()

if entry == "Name":
    print myEmployee.name
    wage = raw_input("Would you like to see their wage?")
    if wage == "Yes":
        print myEmployee.Wage
        exit()
    else:
        print "Okay fine....suit yourself"
        exit()
else:
    print myEmployee.wage
    exit()

