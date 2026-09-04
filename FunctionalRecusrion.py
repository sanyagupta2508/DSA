#Sum of n digits
def func(sum,i,n):
    if i>n:
        print(sum)
    else:
        func(sum+i,i+1,n)

func(0,1,10)

#Aletrnate, using functional recursion

def f(n):
    if n==1:
        return 1
    else:
        return n+f(n-1)

print(f(10))
