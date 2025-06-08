class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        size = len(img1)

        def helper(dx, dy):
            num = 0
            for row in range(size):
                for col in range(size):
                    if 0 <= col + dx < size and 0 <= row + dy < size and img1[row + dy][col + dx] == 1 and img2[row][col] == 1: 
                        num += 1
            return num
    

        return max([helper(dx,dy) for dx in range(-size, size) for dy in range(-size, size)])
     