def maximum69Number(num):
    # Convert number to a list of characters for easy manipulation
    num_str = list(str(num))
    
    # Find the first '6' and change it to '9'
    for i in range(len(num_str)):
        if num_str[i] == '6':
            num_str[i] = '9'
            break  # Only change the first '6'
    
    # Join the list back to a string and convert to integer
    return int("".join(num_str))

# Read input value
num = int(input())

# Print the result
print(maximum69Number(num))