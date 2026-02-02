n=int(input())
numbers=list(map(int,input().split()))
s=-10**9
for i in numbers:
    if s<i:
        s=i
print(s)