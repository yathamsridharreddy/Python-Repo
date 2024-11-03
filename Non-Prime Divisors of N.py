def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
non_prime_count = 0

for i in range(1, N + 1):
    if N % i == 0 and not is_prime(i):
        non_prime_count += 1

print(non_prime_count)