class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = {}
        cols = {}

        #hash tuples for row 
        for row in range(len(grid)): 
            row_tuple = tuple(grid[row])  #makign row into tuple
            if row_tuple not in rows: 
                rows[row_tuple] = 1
            else:
                rows[row_tuple] += 1

        #hash tuples for cols
        for col in range(len(grid[0])): 
            col_tuple = tuple(grid[row][col] for row in range(len(grid)))  
            if col_tuple not in cols: 
                cols[col_tuple] = 1
            else: 
                cols[col_tuple] += 1

        #get mathching pairs bt multiplying 
        for key in rows:
            if key in cols:
                ans += rows[key] * cols[key]

        return ans
