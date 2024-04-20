'''Problem Description
You are given an integer T (number of test cases). You are given array A and an integer B for each test case. You have to tell whether B is present in array A or not.
Problem Constraints
1 <= T <= 10
1 <= A <= 10^5
1 <= A[i], B <= 10^9
Input Format
First line of the input contains number of test cases as single integer T .
Next, each of the test case consists of 3 lines:
First line contains a single integer A denoting the length of array
Second line contains A integers denoting the array elements
Third line contains a single integer B
Output Format
For each test case, print on a separate line 1 if the element exists, else print 0.
Example Input
Input 1:
 1 
 5 
 4 1 5 9 1
 5
Input 2:
 1
 3 
 7 7 2
 1 
Example Output
Output 1: 1 
Output 2: 0 
Example Explanation
Explanation 1:  B = 5  is present at position 3 in A 
Explanation 2:  B = 1  is not present in A. 
'''
#------------------Approach 1 : Using `in` operator--------------------------------#
# T = int(input())
# for _ in range(T):
#     A_length = int(input())
#     A = list(map(int, input().split()))
#     B = int(input())
    
#     if B in A:
#         print(1)
#     else:
#         print(0)
#------------------Approach 2 : without using any builtin function--------------------------------#
T = int(input())
for _ in range(T):
    arr_length = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
for i in range(len(arr)):
    if (arr[i] == target):
        print(1)
        break
    else:
        print(0)
        break
