def is_automorphic(n):
    # Calculate the square of the number
    square = n ** 2
    # Convert both numbers to strings
    str_n = str(n)
    str_square = str(square)
    # Check if the square ends with the number
    if str_square.endswith(str_n):
        return "Automorphic Number"
    else:
        return "Not an Automorphic Number"

# Read input value
n = int(input())

# Print the result
print(is_automorphic(n))