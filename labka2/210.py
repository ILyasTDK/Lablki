n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr.reverse()

for x in arr:
    print(x, end=" ")