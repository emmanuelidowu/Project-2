count=0
def power(n,p):
    global count
    count+=1
    if p==0:
        return 1
    else:
        return n*power(n,p-1)
    
if __name__=='__main__':
    print power(2,0)
    print count
