n=input()
l=[]
b=len(n)
c=[]
for i in n:
    l.append(i)
c=l[::-1]
for j in range(b):
    print(c[j],end="")
