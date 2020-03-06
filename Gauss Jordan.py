def gaussjordan(linear_mtx, solution):
    # Check if the input is a list
    if (type(linear_mtx) != list or type(solution) != list):
        print("The Input must a list")
        return
    matrix_length = len(solution)
    # Check if the matrix is (n x n)
    for i in range(matrix_length):
        if (matrix_length != len(linear_mtx[i])):
            print("The matrix must be n x n")
            return
    # Main Loop
    for i in range(matrix_length):
        # 1) Partial Pivoting
        if (linear_mtx[i][i] < 1): # Check if the pivot is 0 or not, if zero check the next row
            for j in range(i + 1, matrix_length): # Check the next row
                if (abs(linear_mtx[j][i]) > abs(linear_mtx[i] [i])): # If the absolute next row is higher than 0 switch the row
                    for k in range(i, matrix_length):
                        linear_mtx[i][k], linear_mtx[j][k] = linear_mtx[j][k], linear_mtx[i][k] # Switch The Row
                    solution[i], solution[j]=  solution[j], solution[i]
                    break
        # 2) Divison of the pivot row

        # 3) Elimination Loop
        return linear_mtx, solution

# TESTING
a = [[0, 1, 1, 1],
     [3, 0, 3, -4],
     [1, 1, 1, 1],
     [2, 3, 1, 3]]
b = [0, 7, 6, 6]

matrix, solution = gaussjordan(a, b)
print("The elimination matrix is ", matrix)
print("The solution is ", solution)

"""
1) AFTER PIVOTING
The elimination matrix is  [[3, 0, 3, -4], [0, 1, 1, 1], [1, 1, 1, 1], [2, 3, 1, 3]]
The solution is  [7, 0, 6, 6]
2) AFTER DIVISION OF THE PIVOT
The elimination matrix is [[1, 0, 1, -4/3], [0, 1, 1, 1], [1, 1, 1, 1], [2, 3, 1, 3]]
The solution is [7/3, 0, 6, 6]
3) AFTER ELIMINATION LOOP
"""