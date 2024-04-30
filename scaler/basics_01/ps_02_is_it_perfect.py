###
#Problem Description
#Given the Number of Test Cases as T,
#For each test case, take an integer N as input, you have to tell whether it is a perfect number or not.
#
#A perfect number is a positive integer that is equal to the sum of its proper positive divisors (excluding the number itself). 
#A positive proper divisor divides a number without leaving any remainder.
#
#Problem Constraints
#1 <= T <= 10
#1 <= N <= 106
#
#Input Format
#The first line of the input contains a single integer T. 
#Each of the next T lines contains a single integer N.
#
#Output Format
#For each testcase, print YES if the given integer is perfect, else print NO, in a separate line
####
def is_perfect_number(n):
    if n <= 1:
        return False
    
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    
    return divisors_sum == n

# Read the number of test cases
t = int(input())

# Iterate over each test case
for _ in range(t):
    # Read the input number
    n = int(input())
    
    # Check if the number is perfect
    if is_perfect_number(n):
        print("YES")
    else:
        print("NO")
        
