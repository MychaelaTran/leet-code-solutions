class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        newR = len(grid) - 2
        newC = len(grid) - 2
        maxLocal = [["*" for _ in range(newC)] for _ in range(newR)]     

        def helper(x, y):
            num = 0
            for row in range(x, x + 3):
                for col in range(y, y + 3): 
                    if grid[row][col] > num: 
                        num = grid[row][col]
            return num
        
        for i in range(newR): 
            for j in range(newC): 
                maxLocal[i][j] = helper(i,j)

        return maxLocal                

