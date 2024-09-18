'''
Problem Description
You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.
You are to choose 3 trees such that their total cost is minimum. Return that cost.
If it is not possible to choose 3 such trees return -1.


Problem Constraints
1 <= A[i], B[i] <= 109
3 <= size(A) = size(B) <= 3000


Input Format
First argument is an integer array A.
Second argument is an integer array B.


Output Format
Return an integer denoting the minimum cost of choosing 3 trees whose heights are strictly in increasing order, if not possible, -1.


Example Input
Input 1:
 A = [1, 3, 5]
 B = [1, 2, 3]
Input 2:
 A = [1, 6, 4, 2, 6, 9]
 B = [2, 5, 7, 3, 2, 7]


Example Output
Output 1:
 6 
Output 2:
 7 


Example Explanation
Explanation 1:
 We can choose the trees with indices 1, 2 and 3, and the cost is 1 + 2 + 3 = 6. 
Explanation 2:
 We can choose the trees with indices 1, 4 and 5, and the cost is 2 + 3 + 2 = 7. 
 This is the minimum cost that we can get.

'''

def min_cost_trees(A, B):
    n = len(A)
    min_cost = float('inf')
    
    # Iterate over the middle tree q
    for q in range(1, n - 1):
        # Find the minimum cost of the left tree p, where A[p] < A[q]
        left_min_cost = float('inf')
        for p in range(q):
            if A[p] < A[q]:
                left_min_cost = min(left_min_cost, B[p])
        
        # Find the minimum cost of the right tree r, where A[r] > A[q]
        right_min_cost = float('inf')
        for r in range(q + 1, n):
            if A[r] > A[q]:
                right_min_cost = min(right_min_cost, B[r])
        
        # If both left and right trees are found, update the minimum cost
        if left_min_cost != float('inf') and right_min_cost != float('inf'):
            total_cost = left_min_cost + B[q] + right_min_cost
            min_cost = min(min_cost, total_cost)
    
    # If no valid triplet is found, return -1
    return min_cost if min_cost != float('inf') else -1

A = [1, 3, 5]
B = [1, 2, 3]

print(min_cost_trees(A,B))