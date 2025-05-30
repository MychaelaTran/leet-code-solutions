class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #oppoiste of 168
        answer = 0
        power = len(columnTitle) -1
        for char in columnTitle:
            numberLetter = ord(char) - 64   #-64 not 65 to keep from 1-26 not 0-25
            numAdded =  numberLetter * (26**power)
            answer = answer + numAdded
            power -=1


        return answer 
 #example 
#  F   X   S   H   R   X   W
# = 6 * 26^6
# + 24 * 26^5
# + 19 * 26^4
# + 8 * 26^3
# + 18 * 26^2
# + 24 * 26^1
# + 23 * 26^0
        

#chr(65) = A
#chr(90) = Z
# AA = 27, AZ = 52
# BA = 53... 
#ZY = 26 x 26 + 25