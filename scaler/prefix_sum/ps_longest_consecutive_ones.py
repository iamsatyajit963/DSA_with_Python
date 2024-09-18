'''
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.

Input Format
The only argument given is string A.
Output Format
Return the length of the longest consecutive 1’s that can be achieved.
Constraints
1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example
Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
'''
A = "00000000000000000"
def longest_consecutive_ones_with_one_swap(s):
    n = len(A)
    total_ones = A.count('1')
    
    # Edge case: If there are no 1s, return 0
    if total_ones == 0:
        return 0
    
    # Sliding window approach
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(n):
        # Expand the window by adding A[right]
        if A[right] == '0':
            zero_count += 1
        
        # If more than 1 zero in the window, shrink it from the left
        while zero_count > 1:
            if A[left] == '0':
                zero_count -= 1
            left += 1
        
        # Calculate the window length, considering at most one zero swap
        max_len = max(max_len, right - left + 1)
    
    # If all the characters are `1`s, return the total number of 1's
    return min(max_len, total_ones)

print(longest_consecutive_ones_with_one_swap(A))