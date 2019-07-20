a=list(input())
c=0
for i in range(len(a)):
    b=a.count(a[i])
    if(b>c):
        c=b
        d=a[i]
print(d)
