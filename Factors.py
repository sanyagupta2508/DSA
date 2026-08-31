n=36

num=n
result=[]
for i in range(1,num+1):
    if num%i==0:
        result.append(i)
print(result)

#Since factor of any number cannot be more that n/2

result2=[]
for i in range(1,(num//2)+1):
    if num%i==0:
        result2.append(i)
result2.append(num)
print(result2)

#Ideal only for perfect squares-25,36,49,...etc

from math import sqrt
result3=[]
for i in range(1,int(sqrt(num)+1)):
    if num%i==0:
        result3.append(i)
        if num//i!=i:
            result3.append(num//i)
result3.sort()
print(result3)
