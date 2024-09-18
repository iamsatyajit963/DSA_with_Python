a, b = 6,3
# a = 0101
# 1 = 0001
# b = 0011
 
def basics(a,b):
    #AND(&)  ->Only bits that are 1 in both numbers result in 1.
    print(a&b) #0001
    #OR(|) -> If either bit is 1, the result is 1.
    print(a|b)  #0111
    #XOR(^) -> If one of the bits is 1 and the other is 0, the result is 1. Otherwise, it’s 0.
    print(a^b)  #0110
    #NOT(~)
    print(~a)   #1010
    #LEFT SHIFT(<<)
    print(a<<2) #010100
    #RIGHT SHIFT(>>)
    print(a>>2) #0001_ _

    #UC1: Checking odd or even
    if a & 1:
        print("Odd")
    else:
        print("Even")

    #UC 2: Toggling a specific bit
    n = 5  # Binary: 0101
    p = 1  # Toggle the bit at position 1
    result = n ^ (1 << p)  # Binary: 0101 -> 0111 (toggle), result = 7
    print(result)

    #UC 3: Clearing a specific bit
    n = 5  # Binary: 0101
    p = 2  # Clear the bit at position 2
    result = n & ~(1 << p)  # Binary: 0101 -> 0001 (clear), result = 1
    print(result)

#UC 4: count the number of 1 bits (set bits) in a number:
def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1  # If the last bit is 1, increment the count
        n >>= 1  # Right shift to check the next bit
    return count

num = 13  # Binary: 1101
print(count_set_bits(num))  # Output: 3 (since 1101 has 3 set bits)



import math

# 1. Check if a number is a power of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# 2. Find the rightmost set bit
def find_rightmost_set_bit(n):
    return n & -n

# 3. Swap two numbers without a temporary variable
def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# 4. Set, clear, and toggle specific bits
def set_bit(n, p):
    return n | (1 << p)

def clear_bit(n, p):
    return n & ~(1 << p)

def toggle_bit(n, p):
    return n ^ (1 << p)

# 5. Counting the number of set bits (Hamming weight)
def count_set_bits(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

# 6. Reversing the bits in a number
def reverse_bits(n, bit_size=32):
    result = 0
    for i in range(bit_size):
        if n & (1 << i):
            result |= 1 << (bit_size - 1 - i)
    return result

# 7. Convert a decimal number to its binary representation
def decimal_to_binary(n):
    bits = []
    while n > 0:
        bits.append(str(n & 1))
        n >>= 1
    return ''.join(bits[::-1])

# 8. Detect if two integers have opposite signs
def have_opposite_signs(x, y):
    return (x ^ y) < 0

# 9. Turn off the rightmost set bit
def turn_off_rightmost_set_bit(n):
    return n & (n - 1)

# 10. Get the position of the rightmost set bit
def get_position_of_rightmost_set_bit(n):
    return int(math.log2(n & -n)) + 1

# 11. Gray code conversion
def binary_to_gray(n):
    return n ^ (n >> 1)

# 12. Find XOR of all numbers from 1 to n -> pattern
def xor_1_to_n(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

# 13. Detect if the ith bit is set
def is_bit_set(n, i):
    return (n & (1 << i)) != 0

# 14. Rotate bits left and right
def rotate_left(n, d, bit_size=32):
    return (n << d) | (n >> (bit_size - d))

def rotate_right(n, d, bit_size=32):
    return (n >> d) | (n << (bit_size - d))

# 15. Find the missing number in an array
def find_missing_number(arr, n):
    xor_sum = 0
    for i in range(1, n + 1):
        xor_sum ^= i
    for num in arr:
        xor_sum ^= num
    return xor_sum
