def is_pronic_number(x):
    n = 0
    while n * (n + 1) <= x:
        if n * (n + 1) == x:
            return "YES"
        n += 1
    return "NO"

# Read input value
x = int(input())

# Print the result
print(is_pronic_number(x))