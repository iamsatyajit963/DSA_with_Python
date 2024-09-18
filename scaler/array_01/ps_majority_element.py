'''
Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.


Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109


Input Format
Only argument is an integer array.


Output Format
Return an integer.


Example Input
Input 1:
[2, 1, 2]
Input 2:
[1, 1, 1]


Example Output
Input 1:
2
Input 2:
1


Example Explanation
For Input 1:
2 occurs 2 times which is greater than 3/2.
For Input 2:
 1 is the only element in the array, so it is majority
 '''

#Approach 1 : TC -> O(N) | SC -> O(N)

from collections import defaultdict

def majorityElement(nums):
    n = len(nums)
    count_map = defaultdict(int)
    
    # Step 1: Count the occurrences of each element
    for num in nums:
        count_map[num] += 1
        
    # Step 2: Find the element that occurs more than n//2 times
    for num, count in count_map.items():
        if count > n // 2:
            return num

# Test cases
nums1 = [2, 1, 2]
nums2 = [1, 1, 1]
print(majorityElement(nums1))  # Output: 2
print(majorityElement(nums2))  # Output: 1

#Approach2 | Boyer-Moore Voting algorithm | TC O(N) | SC-> O(1)
def majorityElementBMV(nums):
    candidate = None
    count = 0
    
    # First pass: Finding a candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Since the majority element always exists, return the candidate
    return candidate

# Test cases
nums1 = [2, 1, 2]
nums2 = [1, 1, 1]
print(majorityElementBMV(nums1))  # Output: 2
print(majorityElementBMV(nums2))  # Output: 1