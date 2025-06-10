class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = [] #make list, bc string += makes things slower bc craetes new string every time 
        count1, count2 = 0, 0
        while count1 < len(word1) and count2 < len(word2):
            ans.append(word1[count1]) #add word1 letter first
            ans.append(word2[count2]) #add word2 letter second 
            count1 += 1
            count2 += 1

        #add remaining of longer word
        ans.extend(word1[count1:])
        ans.extend(word2[count2:])

        return ''.join(ans)
