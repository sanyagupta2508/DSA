#Head Recursion

def head(i,n):
    if i==n:
        return 0
    else:
        print(i)
        head(i+1,n)

head(1,20)

#Tail Recursion (BackTracking)

def tail(i,n):
    if i==n:
        return 0
    else:
        tail(i+1,n)
        print(i)

tail(1,20)