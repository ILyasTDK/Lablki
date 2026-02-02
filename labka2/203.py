n=int(input())
numbers=list(map(int,input().split()))
s=0
for i in numbers:
    s+=i
print(s)