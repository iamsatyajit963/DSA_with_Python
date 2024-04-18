'''
Problem Description
Given an integer array A of size N and an integer B, you have to print the same array after rotating it B times towards the right.
Problem Constraints
1 <= N <= 106
1 <= A[i] <=108
1 <= B <= 109
Input Format
There are 2 lines in the input
Line 1: The first number is the size N of the array A. Then N numbers follow which indicate the elements in the array A.
Line 2: A single integer B.
Output Format
Print array A after rotating it B times towards the right.
Example Input
Input 1 :
4 1 2 3 4
2
Example Output
Output 1 :
3 4 1 2
Example Explanation
Example 1 :
N = 4, A = [1, 2, 3, 4] and B = 2.
Rotate towards the right 2 times - [1, 2, 3, 4] => [4, 1, 2, 3] => [3, 4, 1, 2]
Final array = [3, 4, 1, 2]
'''

def rotate_array(n, arr, k):
    k = k % n # Handle cases where k > len(lst) | For instance, if arr has a length of 5 and k is 7, it's equivalent to rotating by 2 positions (7 % 5 = 2). So, k %= len(arr) adjusts k to be within the range of 0 to len(lst)-1, ensuring that we're rotating by a valid number of positions.
    rotated_arr = arr[-k:] + arr[:-k]
    return rotated_arr

# Read input
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Rotate the array
rotated_arr = rotate_array(n,arr, k)

# Print the rotated array
print(*rotated_arr)
