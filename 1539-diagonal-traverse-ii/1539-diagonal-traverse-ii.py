class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        #group by diagonal 
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append((i, nums[i][j]))  
                #number on diagonal have same i + j value 
                #store the row along with it 
        
        result = []

        #traverse and build 
        for diag_index in sorted(diagonals.keys()):
            #get curr diag elemetns and append in dec row order (bottom -top)
            diagonal_elements = sorted(diagonals[diag_index], reverse=True)
            
            #add just value, dont matter abt row idnex
            for row, value in diagonal_elements:
                result.append(value)
        
        return result
