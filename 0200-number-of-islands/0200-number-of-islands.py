class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0 
        seen = set()
        q = deque()
        for rows in range(len(grid)):
            for cols in range(len(grid[0])): 
                if (rows, cols) not in seen and grid[rows][cols] == "1":
                    ans += 1 
                    q.append([rows, cols])
                    while q: 
                        row, col = q.popleft()
                        if row > 0: 
                            if grid[row - 1][col] == "1" and (row - 1, col) not in seen: 
                                seen.add((row- 1, col))
                                q.append((row-1, col))
                            
                        if row < len(grid) - 1: 
                            if grid[row + 1][col] == "1" and (row + 1, col) not in seen:
                                seen.add((row+ 1, col))
                                q.append((row+1, col))
                        
                        if col > 0: 
                            if grid[row][col -1] == "1" and (row, col - 1) not in seen: 
                                seen.add((row, col- 1))
                                q.append((row, col -1))

                        if col < len(grid[0]) - 1: 
                            if grid[row][col +1] == "1" and (row,col + 1) not in seen: 
                                seen.add((row, col+ 1))
                                q.append((row, col +1))
                

        return ans 