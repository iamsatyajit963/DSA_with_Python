'''
Problem Description
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.
Note:
Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.
Problem Constraints
1 <= N <= 10^5
-10^5 <= A[i] <= 10^5
Input Format
First arugment is an array A .
Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.
Example Input
Input 1:    A = [-7, 1, 5, 2, -4, 3, 0]
Input 2:    A = [1, 2, 3]
Example Output
Output 1:   3
Output 2:   -1
Example Explanation
Explanation 1:
i   Sum of elements at lower indexes    Sum of elements at higher indexes
0                   0                                   7
1                  -7                                   6
2                  -6                                   1
3                  -1                                  -1
4                   1                                   3
5                  -3                                   0
6                   0                                   0
3 is an equilibrium index, because: A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Explanation 1:
i   Sum of elements at lower indexes    Sum of elements at higher indexes
0                   0                                   5
1                   1                                   3
2                   3                                   0
Thus, there is no such index.
'''
def equilibrium_index(A):
    n = len(A)
    prefix_sum = [0] * n
    suffix_sum = [0] * n

    # Calculate prefix sum
    prefix_sum[0] = A[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + A[i]

    # Calculate suffix sum
    suffix_sum[n-1] = A[n-1]
    for i in range(n-2, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + A[i]

    # Find equilibrium index
    for i in range(n):
        if prefix_sum[i] == suffix_sum[i]:
            return i

    return -1

# def equilibrium_index(A):
#     N = len(A)
#     for i in range(N):
#         left_sum = sum(A[:i])
#         right_sum = sum(A[i+1:])
#         if left_sum == right_sum:
#             return i
#     return -1

# Test the function
A = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium_index(A))  # Output: 3

A = [1, 2, 3]
print(equilibrium_index(A))  # Output: -1
