a=int(input("enter the value 1:"))
b=int(input("enter thr value 2:"))
mul=1
for i in range(1,a):
    if a%i and b%i==0:
        mul=mul+i
c=a*b

if c%mul==0:
    print("yeah")
else:
    print("nah")
