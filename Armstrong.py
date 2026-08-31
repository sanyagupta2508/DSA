n=153

nod= len(str(n))
num=n
total=0
while num>0:
    last_digit=num%10
    total=total+(last_digit**nod)
    num=num//10
print(total==n)
