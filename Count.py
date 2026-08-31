n=5873
num=n
#Using Digit Extraction
count=0
while num>0:
    count=count+1
    num=num//10

print(count)

#Usig logarithm
from math import *

def countDigits(num):
    return int(log10(num)+1)