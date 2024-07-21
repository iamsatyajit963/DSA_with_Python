A = [[1, 2, 3],   
     [4, 5, 6],   
     [7, 8, 9],
     [10, 11, 12]]  
# Square matrix
B = [[9, 8, 7],   
     [6, 5, 4],   
     [3, 2, 1]]

C = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]

#indices of a 2D array
print("Indices of a 2D array: ")
for i in range(len(B)):  
    for j in range(len(B[i])):  
        # 00 01 02 10 11 12 20 21 22
        print(i, j, end = " ")
    print()
print()
print("*"*10)
# Accessing elements of a 2D array
print("Accessing elements of a 2D array: ")
for i in range(len(A)):  
    for j in range(len(A[i])):  
        print(A[i][j], end = " ")  
print()
print("*"*10)

# Printing a 2D array sum row-wise
print("Row wise sum: ")
for i in range(len(A)):  
    sum = 0  
    for j in range(len(A[i])):  
        sum += A[i][j]  
    print("Sum of ", i + 1, " row: ", sum)

print("*"*10)

# Printing a 2D array sum column-wise
print("Column wise sum: ")
for i in range(len(A[0])):  
    sum = 0  
    for j in range(len(A)):  
        sum += A[j][i]  
    print("Sum of ", i + 1, " column: ", sum)
    
print("*"*10)
print("Transpose of a matrix: ")
# Transpose of a matrix
result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print(result)

print("*"*10)
print("Left Diagonal elements of a matrix: ")
# Left Diagonal elements of a matrix
for i in range(len(B)):
    for j in range(len(B[i])):
        if i == j:
            print(B[i][j], end = " ")
# Right Diagonal elements of a matrix
print()
print("Right Diagonal elements of a matrix: ")
i = 0
j = len(B) - 1
while (i < len(B)):
    print(B[i][j], end = " ")
    i += 1
    j -= 1

print()
print("*"*10)


# print all right diagonal like -> 1, 2, 6, 3, 7, 11, 4, 8, 12, 16
print("Right Diagonal elements of a matrix: ")
for c in range(len(C)):
    i = 0
    j = c
    while j >= 0 and i < len(C):
        print(C[i][j], end = " ")
        i += 1
        j -= 1
    print()

print()    
print("*"*10)

# Rotate 90 degree to the right -> transpose and swap every row
print("Rotate 90 degree to the right: ")

print(C)
transpose_result = [[C[j][i] for j in range(len(C))] for i in range(len(C[0]))]
#swap every row
for i in range(len(transpose_result)):
    transpose_result[i] = transpose_result[i][::-1]
print(transpose_result)

print()
print("*"*10)
# add two matrices
X = [[1, 2, 3],   
     [4, 1, 2],   
     [7, 8, 9]]  

Y = [[9, 9, 7],   
     [1, 2, 4],   
     [4, 6, 3]]

for i in range(len(X)):
    for j in range(len(X[i])):
        print(X[i][j] + Y[i][j], end = " ")
    print()
