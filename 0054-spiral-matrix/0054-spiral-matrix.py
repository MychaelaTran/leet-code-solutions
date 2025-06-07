class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        x, y = 0, 0
        dx, dy = 1, 0

        for _ in range(rows*cols):
            ans.append(matrix[y][x])
            #mark now as visited with a marker
            matrix[y][x] = "M"
            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y + dy][x + dx] == "M":
                #change the firection 
                dx_copy = copy.deepcopy(dx)
                dx = -dy
                dy = dx_copy
            
            x += dx
            y += dy
        
        return ans