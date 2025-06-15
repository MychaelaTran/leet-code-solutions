class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        ans = 0 
        temp = 0
        vowels = set("aeiou")
        for i in range(len(s) - k+1): 
            
            if i == 0: #see og window
                for j in range(k): 
                    if s[j] in vowels: 
                        temp += 1
                if temp > ans: 
                    ans = temp
                print("this is temp1 ", temp)
            
            else: 
                if s[i-1] in vowels: 
                    temp -= 1
                if s[i+k-1] in vowels: 
                    temp += 1
                if temp > ans: 
                    ans = temp
                print("this is temp2 ", temp)


        return ans 
        