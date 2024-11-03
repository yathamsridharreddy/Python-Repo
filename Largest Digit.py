def largest_digit(n):
    max_digit = 0
    for digit in str(n):
        max_digit = max(max_digit, int(digit))
    return max_digit

n = int(input())
print(largest_digit(n))