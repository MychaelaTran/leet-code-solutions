class Solution:
    def longestPalindrome(self, s: str) -> str:
        #every character is a palindome 
        #if odd palindrome, middle char no match
        #even lemgth palindrom eacj same

        res = ""
        longest = 0

        #check odd length
        for i in range(len(s)): 
            l, r = i, i #center ptrs

            while l >=0 and r < len(s) and s[l] == s[r]:
                temp = r - l +1
                if temp > longest: 
                    res = s[l:r+1]
                    longest = temp
                l-= 1
                r+= 1
        
        #even length palindoems 
        for i in range(len(s)):
            l, r = i, i +1
            while l >=0 and r < len(s) and s[l] == s[r]:
                temp = r - l +1
                if temp > longest: 
                    res = s[l:r+1]
                    longest = temp
                l-= 1
                r+= 1
        
        return res
