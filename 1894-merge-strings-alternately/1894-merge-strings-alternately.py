class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count1 = 0
        count2 = 0 
        index = 0
        ans = ""
        while count1 < len(word1) and count2 < len(word2): 
            if index % 2 == 0: 
                ans += word1[count1]
                count1 += 1
                index += 1
            else: 
                ans += word2[count2]
                count2 += 1
                index += 1
        
        if count1 < len(word1): 
            ans += word1[count1:]
        
        if count2 < len(word2): 
            ans += word2[count2:]
        
        return ans
        