class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col_with_zero=set()
        row_with_zero=set()
        row=len(matrix)
        col=len(matrix[0])

        for r in range(0,row):
            for c in range(0,col):
                if matrix[r][c]==0:
                    row_with_zero.add(r)
                    col_with_zero.add(c)
        
        for i in row_with_zero:
            for c in range(0,col):
                matrix[i][c]=0

        for i in col_with_zero:
            for r in range(0,row):
                matrix[r][i]=0
        return matrix
