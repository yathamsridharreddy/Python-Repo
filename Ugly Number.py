def is_ugly_number(n):
    if n <= 0:
        return "Not Ugly Number"
    
    for prime in [2, 3, 5]:
        while n % prime == 0:
            n //= prime
    
    return "Ugly Number" if n == 1 else "Not Ugly Number"

n = int(input())
print(is_ugly_number(n))