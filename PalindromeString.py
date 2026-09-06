s="ABKJJKBA"
n=len(s)
left=0
right=n-1

while left<right:
    if s[left]!=s[right]:
        print("False")
    left+=1
    right-=1
else:
    print("True")

#Using Recursion
def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return func(s,left+1,right-1)

print(palindrome(s,left,right))