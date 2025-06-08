class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        x, y = 0 , 0
        ans = []
        rows = len(mat)
        cols = len(mat[0])
        going_up = True

        while len(ans) < rows * cols:
            #either be going up
            if going_up: 
                while y >= 0 and x < cols: 
                    ans.append(mat[y][x])
                    x += 1
                    y -= 1 #going up, row gets smaller index
                #ourside of bounds
                #reset back inside, either col or row is out of bbounds
                if x == cols: #3-6 example 
                    x -= 1  #go back one col 
                    y += 2 # go back down 2 rows to next arrow
                else: #1-2 example
                    y += 1
                
                going_up = False

            else: #going down
                while y < rows and x >= 0: 
                    ans.append(mat[y][x])
                    x -= 1
                    y += 1

                if y == rows: #8-9
                    y -= 1
                    x += 2

                else: #4-7
                    x += 1  
                going_up = True

        return ans



        