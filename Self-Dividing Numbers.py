def is_self_dividing(number):
    original = number
    while number > 0:
        digit = number % 10
        if digit == 0 or original % digit != 0:
            return False
        number //= 10
    return True

A=int(input())
B=int(input())
self_dividing_numbers = []

for num in range(A, B + 1):
    if is_self_dividing(num):
        self_dividing_numbers.append(num)

print(" ".join(map(str, self_dividing_numbers)))