'''
Problem Description
Given an array A of size N. You will be given M queries to process. Each query will be of the form B[i][0] B[i][1].
If the subarray from B[i][0] to B[i][1] is non decreasing, the output should be 1 else output should be 0.
Return an array of integers answering each query.
Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9
1 <= M <= 10^5
0 <= B[i][0], B[i][1] <= N-1
Input Format
First argument contains the array A.
Second argument contains B, denoting the queries.
Output Format
Return an array of integers consisting of 0 and 1
Example Input
Input 1:
A = [1, 7, 3, 4, 9]
B = [[0, 1],[1, 4]]
Input 2:
A = [1, 1, 7, 2, 3]
B = [[0, 2],[2, 4]]
Example Output
Output 1 :[1, 0]
Output 2 :[1, 0]
'''
def non_decreasing_subarray(A, B):
    result = []
    for query in B:
        start = query[0]
        end = query[1]
        subarray = A[start:end+1]
        is_non_decreasing = True
        for i in range(len(subarray) - 1):
            if subarray[i] > subarray[i+1]:
                is_non_decreasing = False
                break
        if is_non_decreasing:
            result.append(1)
        else:
            result.append(0)
    return result

# Example usage
A = [1, 7, 3, 4, 9]
B = [[0, 1], [1, 4]]
output = non_decreasing_subarray(A, B)
print(output)  # [1, 0]

# def non_decreasing_subarray(A, B):
#     result = []
#     for query in B:
#         start = query[0]
#         end = query[1]
#         subarray = A[start:end+1]
#         if subarray == sorted(subarray):
#             result.append(1)
#         else:
#             result.append(0)
#     return result

# # Example usage
# A = [1, 7, 3, 4, 9]
# B = [[0, 1], [1, 4]]
# output = non_decreasing_subarray(A, B)
# print(output)  # [1, 0]
