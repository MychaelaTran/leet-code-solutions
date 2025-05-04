class Solution:
    #Dhiren Booyer Moore
    #this is naive approach O(n*m)
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        index = 0
        for i in range(len(haystack)):
            #initialize to zero every time 
            index = 0
            for j in range(i, i + length):
                if j < len(haystack): #need j to be in bounds of len of haystack since adding len(needle) to i
                    if haystack[j] == needle[index]: 
                        index += 1
                else: 
                    break
            if index == length : 
                return i 
            
            
         
        return -1