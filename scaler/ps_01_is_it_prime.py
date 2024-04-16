####
# Problem Description
# Take an integer A as input, you have to tell whether it is a prime number or not.
# A prime number is a natural number greater than 1 which is divisible only by 1 and itself.
# 
# Problem Constraints
# 1 <= A <= 10**6
# 
# Input Format
# First and only line of the input contains a single integer A.
# 
# Output Format
# Print YES if A is a prime, else print NO.
####
# Approach
# If A is 1, return 'NO'
# If A is 2, return 'YES'
# If A is even, return 'NO'
# If A is odd, check if it is divisible by any number from 2 to sqrt(A) + 1
# If it is divisible by any number, return 'NO'
# Else return 'YES'
# Time Complexity
# O(sqrt(A))
# Space Complexity
# O(1)
####
import time
def is_it_prime(A):
    if A == 1:
        return 'NO'
    if A == 2:
        return 'YES'
    for i in range(2, int(A**0.5) + 1, 2):
        if A % i == 0:
            return 'NO'
    return 'YES'

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    start_time = time.time()
    print(f"Number of factors of {n} is {is_it_prime(n)}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
