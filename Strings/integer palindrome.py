#num to string palindrome
num=1221
s=str(num)
if s ==(s[num::-1]):
    print("yes")
else:
    print("no")

#integer with use input
num=int(input("enter the numbher "))
original = num
rev= 0
while  num>0:
    digit = num % 10
    rev=rev * 10+digit
    num = num //10
if original == rev:
    print("yes ")
else:
    print("No ")