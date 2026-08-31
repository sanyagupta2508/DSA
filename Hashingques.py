# Without hashing
# check the frequency of elements of m in n.
# constraints:- 1) 1 <= n[i] <= 10
#               2) n can have 10^8 elements
#               3) m can have 1068 elements

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
for i in m:
    count=0
    for j in n:
        if j==i:
            count+=1
    print(count)

# Using hashing
# Prestoring values in some datastructure like list/dictionary/set and then fetching it.

hash_list = [0] * 11
for num in n:
    hash_list[num]+=1
for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])

# alternate

freq_dict = {}
num = len(n)
for i in range (0,num):
    freq_dict[n[i]]=freq_dict.get(n[i],0)+1
print(freq_dict)
for j in m:
    if j < 0 or j > 10:
    
        print(0)
    else:
        print(freq_dict.get(j,0))