n = int(input())
count = {}

for _ in range(n):
    number = input()
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

result = 0
for c in count.values():
    if c == 3:
        result += 1

print(result)