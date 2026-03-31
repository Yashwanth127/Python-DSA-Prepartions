# this one is also one way to get rev index way
s="yashwanth "
n=len(s)
for i in range(n-1,-1,-1):
    print(s[i])

s="yashwanth"
n=len(s)
ans=""
for i in range(n-1,-1,-1):
    ans=ans+s[i]
print(ans)

#built in function
s="yashwanht"
print(s[::-1])