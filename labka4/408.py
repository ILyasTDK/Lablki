def primes_up_to(n):
    for num in range(2, n + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

n = int(input())
print(" ".join(map(str, primes_up_to(n))))