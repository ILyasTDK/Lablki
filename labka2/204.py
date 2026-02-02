n=int(input())
numbers=list(map(int,input().split()))
s=0
for i in numbers:
    if i>0:
        s+=1
print(s)