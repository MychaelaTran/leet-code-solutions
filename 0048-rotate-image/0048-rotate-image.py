class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        #need to transpond and then reverse it's x 
        print("orignal matrix ", matrix)
        #transpod
        for row in range(length):
            for col in range(row):
                matrix[row][col], matrix[col][row] =matrix[col][row], matrix[row][col]

        #[list from 321 to 123]
        for row in matrix:
            row.reverse()
        

        return matrix



