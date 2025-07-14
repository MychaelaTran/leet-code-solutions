class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0]) -1 
        rows = len(matrix) - 1

        row_high = rows 
        row_low = 0
        ans_row = -1

        while row_low <= row_high: 
            mid = (row_low+ row_high) //2

            if mid == 0: 
                if matrix[mid][0] <= target <= matrix[mid][cols]: 
                    ans_row = mid
                    break
            
            #do normal and check row before 
            if matrix[mid-1][cols] < target <= matrix[mid][cols]:
                ans_row = mid
                break
            elif matrix[mid][cols] < target: 
                row_low = mid + 1
            else: 
                row_high = mid -1
        
        print(ans_row)

        #do binary serach on col 
        col_low = 0
        col_high = cols
        while col_low <= col_high: 
            mid = (col_low + col_high) //2
            if matrix[ans_row][mid] == target: 
                return True
            elif matrix[ans_row][mid] > target: 
                col_high = mid - 1
            else: 
                col_low = mid + 1
        
        return False
            
        return 
        