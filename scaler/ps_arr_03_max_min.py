'''
Problem Description
Take input an array A of size N and write a program to print maximum and minimum elements of the input. The only line of the input would contain a single integer N that represents the length of the array followed by the N elements of the input array A.
Problem constraints
1 <= N <= 1000
1 <= A <= 1000
Input Format
The first line contains a single integer N representing the length of the array A followed by N elements of the array A.
Output Format
A single line output containing two space-separated integers.
The first integer is the maximum value of the array.
The second integer is the minimum value of the array. 
There is **no space** after the minimum value in the output format. 
There is only a **single space** between the maximum and minimum value.
Example Input
Input 1:
5 1 2 3 4 5
Input 2:
4 10 50 40 80
Example Output
Output 1:
5 1
Output 2:
80 10
Note: There is no space after the minimum value in the output format.
There is only a single space between the maximum and minimum value.
'''

def find_max_min_brute_force(arr):
    # Initialize max and min with the first element of the array
    max_val = arr[0]
    min_val = arr[0]
    
    # Iterate through the array to find max and min
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    
    return max_val, min_val

# Taking input
n, *arr = map(int, input().split())
max_val, min_val = find_max_min_brute_force(arr)
print(max_val, min_val, sep=' ')
#--------------------------------------#
# # Read the input
# n, *arr = map(int, input().split())

#--------------------------------------#
# # Find the maximum and minimum values
# max_val = max(arr)
# min_val = min(arr)

# # Print the result
# print(max_val, min_val, end='')
#---------------------------------------#
# # Sort the array in ascending order
# arr.sort()

# # Print the result
# print(arr[-1], arr[0], end='')
