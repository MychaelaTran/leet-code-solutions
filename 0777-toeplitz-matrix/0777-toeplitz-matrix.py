class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Check horizontal diagonals starting from top row
        for col_start in range(cols): 
            ref = matrix[0][col_start]
            row = 1
            col = col_start + 1
            while row < rows and col < cols:
                print("checking", matrix[row][col], "against", ref)
                if matrix[row][col] != ref:
                    return False
                row += 1
                col += 1
        
        # Check vertical diagonals starting from leftmost column (excluding [0][0])
        for row_start in range(1, rows):
            ref = matrix[row_start][0]
            row = row_start + 1
            col = 1
            while row < rows and col < cols:
                print("checking", matrix[row][col], "against", ref)
                if matrix[row][col] != ref:
                    return False
                row += 1
                col += 1
        
        return True
