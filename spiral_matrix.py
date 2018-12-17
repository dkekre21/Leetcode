import numpy as np
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = int(np.shape(matrix)[0]), int(np.shape(matrix)[1])
        k, l = 0, 0
        last_row = m-1
        last_col = n-1
        while k<=last_row and l<=last_col:
            for i in range(l, last_col+1):
                print (matrix[k][i])
            k += 1 # increment row
            for i in range(k, last_row+1):
                print (matrix[i][last_col])
            last_col -= 1 # decrement the last column
            if (k<=last_row):
                for i in range(last_col, l-1, -1):
                     print (matrix[last_row][i])
                last_row -= 1
            if (l<= last_col):
                for i in range(last_row, k-1, -1):
                     print (matrix[i][l])
                l += 1       