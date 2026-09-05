#Reverse the array from index 2 to 7

arr=[5,7,3,9,4,7,4,6,4,9]
arr1=arr[2:8]
arr2=arr[0:2]
arr3=arr[8:10]
reversed_arr=arr1[::-1] #arr1.reverse() can also be used
print(arr2+reversed_arr+arr3)

#Using Recursion
arr=[5,7,3,9,4,7,4,6,4,9]

def ArrayReversing(num,left,right):
    if left>=right:
        return num
    else:
        num[left],num[right]=num[right],num[left]
        return ArrayReversing(num,left+1,right-1)

print(ArrayReversing(arr,2,7))

