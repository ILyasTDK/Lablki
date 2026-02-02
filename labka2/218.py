n = int(input())
arr = [input() for _ in range(n)]
printed = []

for s in sorted(arr):
    if s not in printed:
        print(s, arr.index(s) + 1)
        printed.append(s)
