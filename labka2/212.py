n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = arr[i] ** 2

for x in arr:
    print(x, end=" ")