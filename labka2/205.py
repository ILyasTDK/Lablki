n=int(input())
n1=n
a=1000000000000
s=0
while a>0:
    if n%2==0:
        s+=1
    else:
        break
    n/=2
    a-=1
if n1==2**s:
    print("YES")
else:
    print("NO") 