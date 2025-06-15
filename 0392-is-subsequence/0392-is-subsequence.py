class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = len(t) - 1
        n = 0
        m = len(s) -1
        count = 0


        while left < right and n <= m: 
            if t[left] == s[n]: 
                left += 1
                n += 1
                count += 1
            elif t[right] == s[m]: 
                m -= 1
                right -= 1
                count += 1
            else: 
                left += 1
                right -= 1
        if left == right and count != len(s) and t[left] == s[n]:
            count += 1
        if count == len(s): 
            return True
        
        else:
            return False