def reverse_integer(N):
    
    sign = -1 if N < 0 else 1
    
    
    reversed_num = int(str(abs(N))[::-1]) * sign
    
    
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    return reversed_num


N = int(input())


print(reverse_integer(N))