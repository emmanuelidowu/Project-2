entry=raw_input("Type in a number")
def countdown(n):
    while n > 0:
        print(n)
        n = n -1
    if n<=0:
        print('ZeroTime')

countdown(int(entry))

