n = int(input())
nums = list(map(int, input().split()))

max_value = nums[0]
position = 1

for i in range(1, n):
    if nums[i] > max_value:
        max_value = nums[i]
        position = i + 1

print(position)
