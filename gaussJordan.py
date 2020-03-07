def gaussjordan(matrix, sol):
    # Check if the input is a list
    if (type(matrix) != list or type(sol) != list):
        print("The Input must a list")
        return
    row_length = len(matrix)
    # Check if the matrix is (n x n)
    for i in range(row_length):
        if (row_length != len(matrix[i])):
            print("The matrix is incorrect")
            return
    # Mix the matrix and the solution
    for i in range(row_length):
        matrix[i].append(sol[i])
    # Gauss Jordan Elimination
    try:
        # Main Loop
        for i in range(row_length):
            # 1) Partial Pivoting
            if (matrix[i][i] == 0):
                for j in range(row_length + 1):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i + 1][j]
                    matrix[i + 1][j] = temp
            # 2) Parameter for division
            if (matrix[i][i] != 1):
                par = matrix[i][i]
                for j in range(row_length + 1):
                    matrix[i][j] = matrix[i][j] / par
            # 3) Substraction
            for j in range(i + 1, row_length):
                par = matrix[j][i]
                for k in range(row_length + 1):
                    matrix[j][k] = matrix[j][k] - par * matrix[i][k]
            # 4) Elimination
            for i in range(row_length):
                for j in range(0, row_length - 1 - i):
                    par = matrix[j][row_length - 1 - i]
                    for k in range(row_length + 1):
                        matrix[j][k] = matrix[j][k] - par * matrix[row_length - 1 - i][k]
        # Change the -0.0 to 0.0
        for i in range(row_length):
            for j in range(row_length + 1):
                if(matrix[i][j] == -0):
                    matrix[i][j] = 0.0
        solution = list()
        # Separate the matrix and the solution
        for i in range(row_length):
            sol = matrix[i].pop(row_length)
            solution.append(sol)
        return matrix, solution
    except(err):
        print("The Matrix has Trivial Solution")
        return 


def main():
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

if (__name__ == '__main__'):
	main()
