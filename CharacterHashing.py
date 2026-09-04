s="azyxyyzaaadjbkelidh"
q=["d","a","y","x","f","l"]

#Constraint=> s can hold only the small alphabets i.e a to z
#Ques. Find out the number of occurence of character in q in the string s

hash_list=[0]*26

for ch in s:
    ascii_value=ord(ch)
    index=ascii_value-97
    hash_list[index]+=1

for ch in q:
    ascii_value=ord(ch)
    index=ascii_value-97
    print(hash_list[index])

