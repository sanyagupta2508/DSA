num=[5,8,2,7,9,1,6,4,3]

def SelectionSort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr

print(SelectionSort(num))
