'''
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
Problem Constraints
1 <= N <= 10^5
-10^5 <= A[i] <= 10^5
Sum of all elements of A <= 10^9
Input Format
First argument contains an array A of integers of size N
Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
Example Input
Input 1:A = [2, 1, 6, 4]
Input 2:A = [1, 1, 1]
Example Output
Output 1:1
Output 2:3
Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 
Explanation 2:
Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.
'''
def count_indices(A):
    even_sum = sum(A[::2])  # sum of even-indexed elements
    odd_sum = sum(A[1::2])  # sum of odd-indexed elements
    count = 0
    for i in range(len(A)):
        if (i % 2 == 0 and even_sum - A[i] == odd_sum) or (i % 2 != 0 and odd_sum - A[i] == even_sum):
            count += 1
    return count

# Test cases
A1 = [2, 1, 6, 4]
A2 = [1, 1, 1]
print(count_indices(A1))  # Output: 1
print(count_indices(A2))  # Output: 3
