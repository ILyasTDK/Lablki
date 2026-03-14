n = int(input())
numbers = map(int, input().split())

result = sorted(set(numbers))

print(*result)