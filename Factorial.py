num=10
fact=1
if num>0:
    for num in range (1,num+1):
        fact=fact*num
    print(fact)


#Using recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(10))