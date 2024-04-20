'''
Problem Description
You are given a constant array A.
You are required to return another array which is the reversed form of the input array.
Problem Constraints
1 <= A.size() <= 10000
1 <= A[i] <= 10000
Input Format
First argument is a constant array A.
Output Format
Return an integer array.
Example Input
Input 1:A = [1,2,3,2,1]
Input 2:A = [1,1,10]
Example Output
Output 1: [1,2,3,2,1] 
Output 2: [10,1,1] 
Example Explanation
Explanation 1:Reversed form of input array is same as original array
Explanation 2:Clearly, Reverse of [1,1,10] is [10,1,1]
'''
#------------------Approach 1--------------------------------#
# arr = input()
# print(arr[::-1])
#------------------Approach 2--------------------------------#
# SWAPing mechanism
# def reversearr(arr):
#     s = 0
#     e = len(arr)-1
#     while(s < e):
#         temp = arr[s] 
#         arr[s] = arr[e]
#         arr[e] = temp
#         s += 1
#         e -= 1
#     print(arr)
# arr = list(map(int, input().split()))
# reversearr(arr)
#------------------Approach 2.a--------------------------------#
# SWAPing mechanism without using third variable
def reversearr(arr):
    s = 0
    e = len(arr)-1
    while(s < e):
        arr[s], arr[e] = arr[e], arr[s] #Tricks in python
        s += 1
        e -= 1
    print(arr)
arr = list(map(int, input().split()))
reversearr(arr)
