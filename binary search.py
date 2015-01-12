a=[12,73,82,91,5,78,54,32,98,96]
a.sort()

xy=int(raw_input("Enter a number to see if its in the list"))

def binSearch(listx, key):
    mid = len(listx)/2
    if listx[mid] == key:
        return True
    elif len(listx) == 1:
        return False
    elif listx[mid] > key:
        left = listx[:mid]
        return binSearch(left, key)
    else:
        right = listx[mid:]
        return binSearch(right, key)

print binSearch(a, xy)

