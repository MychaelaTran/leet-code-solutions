class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]: 
        ans = [[] for _ in range(r)]
        curr_rows = len(mat)
        curr_cols = len(mat[0])
        if r*c != curr_rows * curr_cols: 
            return mat
        
        new_row = 0
        new_col = 0
        for i in range(curr_rows):
            for j in range(curr_cols):
                if new_col < c:
                    ans[new_row].append(mat[i][j])
                    new_col += 1
                else: 
                    new_col = 1
                    new_row += 1
                    ans[new_row].append(mat[i][j])
        
        return ans



            
        