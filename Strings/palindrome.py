s="mallama"
n=len(s)
ans=""
for i in range(n-1,-1,-1):
    ans = ans +s[i]
if s== ans:
    print("yes ")
else:
    print("no")

#built in function
s="1221"
if s == s[::-1]:
    print("yes ")
else:
    print("no")