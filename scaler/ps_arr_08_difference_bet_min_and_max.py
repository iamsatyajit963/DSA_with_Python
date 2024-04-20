'''
Problem Constraints
2 <= N <= 1e5
-1e9 <= A[i] <= 1e9
There is atleast 1 odd and 1 even number in A
Input Format
The first argument given is the integer array, A.
Output Format
Return maximum among all even numbers of A - minimum among all odd numbers in A.
Example Input
Input 1: A = [0, 2, 9]
Input 2: A = [5, 17, 100, 1]
Example Output
Output 1:-7
Output 2:99
Example Explanation
Explanation 1:
Maximum of all even numbers = 2
Minimum of all odd numbers = 9
ans = 2 - 9 = -7
Explanation 2:
Maximum of all even numbers = 100
Minimum of all odd numbers = 1
ans = 100 - 1 = 99
'''
# even_numbers = [num for num in A if num % 2 == 0]
# odd_numbers = [num for num in A if num % 2 != 0]
# max_even = max(even_numbers)
# min_odd = min(odd_numbers)
# result = max_even - min_odd
# print(result)
#---------------------------------------------------------#
def solve(A):
    max_even = float('-inf')
    min_odd = float('inf')
    
    for num in A:
        if num % 2 == 0 and num > max_even:
            max_even = num
        elif num % 2 != 0 and num < min_odd:
            min_odd = num
    
    return max_even - min_odd

print(solve([1,2,3,4,5]))

