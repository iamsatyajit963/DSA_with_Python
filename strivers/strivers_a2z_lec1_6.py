"""
This program calculates the sum of even and odd digits in a given integer.

The program prompts the user to enter an integer and then iterates through each digit of the integer.
If the digit is even, it adds it to the even_sum variable. If the digit is odd, it adds it to the odd_sum variable.
Finally, it prints the sum of even digits and the sum of odd digits.

Example:
Enter an integer: 123456
12 9
"""
n = int(input("Enter an integer: "))
even_sum = 0
odd_sum = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    n //= 10
print(even_sum," ",odd_sum )
