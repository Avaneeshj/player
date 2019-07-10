n=int(input())
b=0
while(n>0):
    a=n%10
    n=int(n/10)
    b+=a*a
print(b)
