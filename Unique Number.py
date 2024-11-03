def is_unique_number(n):
    # Convert the number to a string
    num_str = str(n)
    
    # Create a set to track unique digits
    seen_digits = set()
    
    # Check each digit
    for digit in num_str:
        if digit in seen_digits:
            return "Not Unique Number"
        seen_digits.add(digit)
    
    return "Unique Number"

# Read input value
n = int(input())

# Print the result
print(is_unique_number(n))