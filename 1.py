s=input()
b=len(s)
l=[]
for i in s:
    l.append(i)
n=[]
n=l[::-1]
for j in range(b):
    print(n[j],end="")
