m = len(matrix)
n = len(matrix[0])
for k in range(m):
    i = k
    j = 0
    while (i>=0):
        print (matrix[i][j])
        i -= 1
        j += 1
for k in range(n-1):
    i = m - 1
    j = k + 1
    while (j<= n-1):
        print (matrix[i][j])
        i -= 1
        j += 1