a=int(input())
b=list(map(str,input()[:a]))
for i in b:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        b.remove(i)
b.reverse()
for j in b:
    print(j,end="")
