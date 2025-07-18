from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: #BFS
        q = deque()
        ans = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        total_oranges = 0

        #find all rotting ones and add to queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    seen.add((i,j))
                    total_oranges += 1
                if grid[i][j] == 1: 
                    total_oranges += 1
        
        if total_oranges == 0: #alr no fresh oranges
            return 0
        
        #get all adhjacent each min 
        while q:
            num_rotten = len(q)
            for _ in range(num_rotten):
                r, c = q.popleft()
                check = [(r +1, c ), (r-1, c), (r, c+1), (r, c-1)]
                for i,j in check: 
                    if i >=0 and i < rows and j >= 0 and j < cols and grid[i][j] == 1 and (i,j) not in seen: 
                        q.append((i,j))
                        seen.add((i,j))

            
            ans += 1
    
        if len(seen) != total_oranges:
            return -1
        
        return ans -1 #when add += ans at end when q is done 

        