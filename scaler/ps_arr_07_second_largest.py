'''
Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.
Problem Constraints
1 <= |A| <= 10^5
0 <= A[i] <= 10^9
Input Format
The first argument is an integer array A.
Output Format
Return the second largest element. If no such element exist then return -1.
Example Input
Input 1: A = [2, 1, 2] 
Input 2: A = [2]
Example Output
Output 1: 1 
Output 2: -1 
Example Explanation
Explanation 1:
 First largest element = 2
 Second largest element = 1
Explanation 2:
 There is no second largest element in the array.
 '''
def find_second_largest(A):
   if len(A) < 2:
       return -1
   largest = max(A[0], A[1])
   second_largest = min(A[0], A[1])
   for i in range(2, len(A)):
       if A[i] > largest:
           second_largest = largest
           largest = A[i]
       elif A[i] > second_largest and A[i] != largest:
           second_largest = A[i]
   if second_largest == float('-inf'):
       return -1
   return second_largest

# Test cases
A = [2, 1, 2]
print(find_second_largest(A))  # Output: 1

A = [2]
print(find_second_largest(A))  # Output: -1
