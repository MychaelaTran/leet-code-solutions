class Solution:
    #Dhiren Booyer Moore
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        index = 0
        answer = 0
        for i in range(len(haystack)):
            #initialize to zero every time 
            index = 0
            while index < len(needle): 
                for j in range(i, i + len(needle)):
                    if j < len(haystack): #need j to be in bounds of len of haystack since adding len(needle) to i
                        if haystack[j] == needle[index]: 
                            index += 1
                    else: 
                        break
                if index == len(needle) : 
                    return i 
                else: 
                    break
            
         
        return -1