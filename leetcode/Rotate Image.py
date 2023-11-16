class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=0
        r=len(matrix)-1
        while l<r:
            for i in range(r-l):
                top=l
                bottom=r
                ##temp variable to store top left
                topleft=matrix[top][l+i]

                matrix[top][l+i]=matrix[bottom-i][l]
                matrix[bottom-i][l]=matrix[bottom][r-i]
                matrix[bottom][r-i]=matrix[top+i][r]
                matrix[top+i][r]=topleft
                
            l=l+1
            r=r-1
        return matrix


