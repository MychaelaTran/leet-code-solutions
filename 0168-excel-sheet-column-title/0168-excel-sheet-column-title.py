class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        firstLetter = math.ceil(columnNumber/26) 

        answer = ""
        

        while columnNumber > 0: 
            columnNumber -= 1 #eg A = 1 but 1 mod 26 gives us 1 when we want 0
            remainder = columnNumber % 26
            answer = chr(65 + remainder) + answer
            columnNumber = columnNumber//26 #make sure to floor it
         
        return answer
            
            
#chr(65) = A
#chr(90) = Z
# AA = 27, AZ = 52
# BA = 53... 