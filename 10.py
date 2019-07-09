a,b=list(map(str,input().split()))
c=len(a)
d=0
for i in range(c):
    if(a[i]!=b[i]):
        d+=1
if(d==1):
    print("yes")
else:
    print("no")
