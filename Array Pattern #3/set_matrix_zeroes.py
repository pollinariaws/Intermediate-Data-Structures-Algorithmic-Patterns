class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_in_row = False
        zero_in_col = False
        row = len(matrix)
        col = len(matrix[0])
        for j in range(col):
            if matrix[0][j] == 0:
                zero_in_row = True
                break
        for i in range(row):
            if matrix[i][0] == 0:
                zero_in_col = True
                break
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if zero_in_row:
            for i in range(col):
                matrix[0][i] = 0
        if zero_in_col:
            for i in range(row):
                matrix[i][0] = 0
                    
                    
