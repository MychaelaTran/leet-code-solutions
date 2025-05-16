class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1) #initalize whole row to zero 
        row[0] = 1 # first and last are always 0
      

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row

        

        