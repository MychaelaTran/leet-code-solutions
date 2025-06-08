class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        dx, dy = 1, 0  #start movcing right
        for num in range(1, n * n + 1):  # fill from 1 to n^2
            ans[y][x] = num

            #check if need to change direction 
            if not (0 <= x + dx < n and 0 <= y + dy < n) or ans[y + dy][x + dx] != 0:
                dx, dy = -dy, dx  #move clockwise 

            x += dx
            y += dy

        return ans
