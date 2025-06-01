class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 1: 
            return 1
        
        ans = 0
        l = 0
        r = 0
        temp = 0
        seen = []

        while r < len(s):
            print("this is s[r]: ", s[r])
            if s[r] not in seen:  
                seen.append(s[r])
                temp += 1
                r += 1
            else: 
                if temp > ans:
                    ans = temp
                to_find = s[r] #the duplicate we need to go up to remove
                print("this is to_find: ", s[r])
                while s[l] != to_find:
                    print("this is s[left]: ", s[l])
                    seen.remove(s[l])
                    l += 1
                    temp -= 1
                seen.remove(s[l])
                l += 1
                temp -=1
        if temp > ans: 
            ans = temp
                
                
                            
        
        return ans
        