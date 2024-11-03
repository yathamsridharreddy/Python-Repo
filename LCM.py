import math

def calculate_lcm(a, b):
    # Calculate LCM using the formula
    return abs(a * b) // math.gcd(a, b)

# Read input values
a, b = map(int, input().split())

# Calculate and print the LCM
print(calculate_lcm(a, b))