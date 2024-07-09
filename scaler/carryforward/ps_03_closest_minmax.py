'''
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.
Problem Constraints	1 <= |A| <= 2000

Input Format
First and only argument is vector A

Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array

Example Input
Input 1:A = [1, 3, 2]
Input 2:A = [2, 6, 1, 6, 9]
Example Output
Output 1: 2
Output 2: 3
Example Explanation
Explanation 1: Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
Explanation 2: Take the last 3 elements of the array.
'''
import sys
A = [1,3,2]
min_val = min(A)
max_val = max(A)

min_index, max_index, ans = -1, -1, sys.maxsize
for i in range(0, len(A)):
    if A[i] == min_val:
        min_index = i
    if A[i] == max_val:
        max_index = i
    if min_index != -1 and max_index != -1:
        ans = min(ans, abs(max_index - min_index) + 1)

print(ans)
