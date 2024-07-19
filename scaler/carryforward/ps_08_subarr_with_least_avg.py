'''
Problem Description
Given an array A of size N, find the subarray of size B with the least average.
Problem Constraints
1 <= B <= N <= 10^5
-10^5 <= A[i] <= 10^5
Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.
Output Format
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.
Example Input
Input 1:	A = [3, 7, 90, 20, 10, 50, 40]	B = 3
Input 2:	A = [3, 7, 5, 20, -10, 0, 12]	B = 2
Example Output
Output 1:	3
Output 2:	4
Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:
 Subarray between [4, 5] has minimum average
'''
def find_subarray_with_least_avg(A, B):
    min_avg = float('inf')
    min_avg_index = 0
    
    # Calculate the sum of the first subarray of size B
    curr_sum = sum(A[:B])
    
    # Update the minimum average and index
    if curr_sum / B < min_avg:
        min_avg = curr_sum / B
        min_avg_index = 0
    
    # Iterate through the remaining subarrays
    for i in range(1, len(A) - B + 1):
        # Update the current sum by subtracting the first element and adding the next element
        curr_sum = curr_sum - A[i - 1] + A[i + B - 1]
        
        # Update the minimum average and index
        if curr_sum / B < min_avg:
            min_avg = curr_sum / B
            min_avg_index = i
    
    return min_avg_index


A = [3, 7, 90, 20, 10, 50, 40]
print(find_subarray_with_least_avg(A, 3))# 3
