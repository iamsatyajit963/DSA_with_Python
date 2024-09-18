'''
Problem Description
Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.
Note: It is possible to swap any two elements, not necessarily consecutive.

Problem Constraints
1 <= length of the array <= 100000
-109 <= A[i], B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return the minimum number of swaps.

Example Input
Input 1:
 A = [1, 12, 10, 3, 14, 10, 5]
 B = 8
Input 2:
 A = [5, 17, 100, 11]
 B = 20

Example Output
Output 1:
 2
Output 2:
 1

Example Explanation
Explanation 1:
 A = [1, 12, 10, 3, 14, 10, 5]
 After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
 After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
 Now, all elements less than or equal to 8 are together.
Explanation 2:
 A = [5, 17, 100, 11]
 After swapping 100 and 11, A => [5, 17, 11, 100].
 Now, all elements less than or equal to 20 are together.
 '''

A = [1, 12, 10, 3, 14, 10, 5]
B = 8



def min_swaps(A, B):
    # Figuring out how many elements are less than that of B
    n = len(A) #7
    count_qualified = sum(1 for x in A if x <= B)
    # print(count_qualified)

    if count_qualified == 0:
        return 0
    
    current_count = 0
    for i in range(count_qualified):
        if A[i] <= B:
            current_count += 1
    # print(current_count)
        # This is the maximum count of elements <= B in a window of size count_qualified
    max_qualified_in_window = current_count
    
    # Step 3: Slide the window across the array
    for i in range(count_qualified, n):
        # Include the new element in the window
        if A[i] <= B:
            current_count += 1
        # Exclude the element that's sliding out of the window
        if A[i - count_qualified] <= B:
            current_count -= 1
        # Update the maximum count of qualified elements in any window
        max_qualified_in_window = max(max_qualified_in_window, current_count)
    
    # Step 4: The minimum swaps needed is the number of unqualified elements in the best window
    min_swaps = count_qualified - max_qualified_in_window
    
    return min_swaps


print(min_swaps(A, B))