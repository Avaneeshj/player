n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,k):
    l=[l[-1]]+l[:-1]
print(*l)
