def is_armstrong_number(num):
    """
    You are given an integer N you need to print all the Armstrong Numbers between 1 to N. (N inclusive).
    If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
    For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).
    """
    # Convert the number to a string to iterate over its digits
    num_str = str(num)
    
    # Calculate the sum of cubes of each digit
    sum_of_cubes = sum(int(digit) ** len(num_str) for digit in num_str)
    
    # Check if the sum is equal to the number itself
    return sum_of_cubes == num

def print_armstrong_numbers(N):
    for num in range(1, N+1):
        if is_armstrong_number(num):
            print(num)

# Test the function
N = int(input("Enter the value of N: "))
print("Armstrong numbers between 1 and", N, "are:")
print_armstrong_numbers(N)
