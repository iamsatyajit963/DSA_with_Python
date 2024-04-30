'''
Problem Description
You are given an integer array A of size N.
You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.
Find and return the maximum possible sum of the B elements that were removed after the B operations.
NOTE: Suppose B = 3, and array A contains 10 elements, then you can:
Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.
Problem Constraints
1 <= N <= 10^5
1 <= B <= N
-10^3 <= A[i] <= 10^3
Input Format
First argument is an integer array A.
Second argument is an integer B.
Output Format
Return an integer denoting the maximum possible sum of elements you removed.
Example Input
Input 1: A = [5, -2, 3 , 1, 2] B = 3
Input 2: A = [ 2, 3, -1, 4, 2, 1 ] B = 4
Example Output
Output 1: 8
Output 2: 9
Example Explanation
Explanation 1: Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2: Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9
'''


def pick_from_both_sides(A, B):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    suffix_sum = [0] * (n + 1)

    # Calculate prefix sum
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    # Calculate suffix sum
    for i in range(n - 1, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + A[i]

    max_sum = float('-inf')

    # Try removing elements from both sides
    for i in range(B + 1):
        max_sum = max(max_sum, prefix_sum[i] + suffix_sum[n - B + i])

    return max_sum

# Test the function
A = [5, -2, 3, 1, 2]
B = 3
print(pick_from_both_sides(A, B))  # Output: 8

A = [2, 3, -1, 4, 2, 1]
B = 4
print(pick_from_both_sides(A, B))  # Output: 9
