import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)): 
            if s[i].isalnum():
                continue
            else: 
                s = s.replace(s[i], " ")
        
        #remove all white spaces added
        s = s.replace(" ", "").lower()

        return s == s[::-1]
                








    #used too much memory             
    #     #use regex to get rid of unwatned chars: 
    #     pattern = r'[^a-zA-Z0-9]' #^... means any character NOT in this set (alphanumeric)
    #     s1 = re.sub(pattern , '', s).lower()

    #     check = self.helper(s1)

    #     return check
    
    # def helper (self, s) -> bool: 
    #     if len(s) <= 1: 
    #         return True
        
    #     if s[0] == s[-1]: 
    #         return self.helper(s[1:-1])
    #     else: 
    #         return False

        