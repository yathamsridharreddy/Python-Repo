def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

N = int(input())
next_num = N + 1

while True:
    if is_prime(next_num) and is_palindrome(next_num):
        print(next_num)
        break
    next_num += 1