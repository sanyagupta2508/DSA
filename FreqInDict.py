num = [5,6,7,7,1,9,111,1,1,5,1,1]

freq_map = {}

for i in range(0, len(num)):

    if num[i] in freq_map:
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1

print(freq_map[7])

#Using Hashing
hash_map={}
n=len(num)
for i in range(0,n):
    hash_map[num[i]]=hash_map.get(num[i],0)+1