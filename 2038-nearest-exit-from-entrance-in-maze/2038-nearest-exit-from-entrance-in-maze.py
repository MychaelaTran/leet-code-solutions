from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        start_row, start_col = entrance
        rows, cols = len(maze), len(maze[0])
        
        q = deque([(start_row, start_col, 0)])
        seen = set([(start_row, start_col)])

        while q:
            row, col, count = q.popleft()
            bounds = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            
            for i, j in bounds:
                if 0 <= i < rows and 0 <= j < cols and (i, j) not in seen and maze[i][j] == ".":
                    if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and (i, j) != (start_row, start_col):
                        return count + 1
                    q.append((i, j, count + 1))
                    seen.add((i, j))

        return -1
