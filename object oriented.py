def program():
    entry = raw_input("Would you like to see wage or name(Capital Letter start)?")
    class Employee:
        def __init__(self):
            self.name=["Dom"]
            self.wage="30000 Pounds"
    myEmployee = Employee()
    if entry == "Name":
        print myEmployee.name
        wage = raw_input("Would you like to see their wage?")
    else:
        print myEmployee.wage
        new = raw_input("Enter a new employee name:")
        myEmployee.name.append(new)
        print myEmployee.name

for i in range(1,100):
    program()

    


