matrix = list()
x = int(input("Enter how many var you want: "))
for i in range(x):
    print('Enter equation ', i+1, ':', sep='')
    matrix.append([])
    for j in range(x+1):
        if (j == x):
            n = int(input("y: "))
        else:
            print('x', j+1, ': ', sep='', end='')
            n = int(input())
        matrix[i].append(n)
print('ARRAY: ',matrix)

#using gauss-jordan elimination
for i in range(x):
    #checking whether matrix[i][i] = 0
    if (matrix[i][i] == 0):
        for j in range(x+1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i+1][j]
            matrix[i+1][j] = temp
    #parameter for division
    if (matrix[i][i] != 1):
        par = matrix[i][i]
        for j in range(x+1):
            matrix[i][j] = matrix[i][j] / par
    #substraction
    for j in range(i+1, x):
        par = matrix[j][i]
        for k in range(x+1):
            matrix[j][k] = matrix[j][k] - par * matrix[i][k]

#finding variable solutions
for i in range(x):
    for j in range(0, x-1-i):
        par = matrix[j][x-1-i]
        for k in range(x+1):
            matrix[j][k] = matrix[j][k] - par * matrix[x-1-i][k]

for i in range(x):
    print('x', i+1, ' = %.2f' % matrix[i][x], sep='')
