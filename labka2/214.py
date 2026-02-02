n = int(input())
arr = list(map(int, input().split()))

most_frequent = arr[0]
max_count = 0

for num in arr:
    count = 0
    for x in arr:
        if x == num:
            count += 1
    if count > max_count or (count == max_count and num < most_frequent):
        max_count = count
        most_frequent = num

print(most_frequent)
