class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        #larger iteration
        #iteratre through each word
        #each iteration check the ith letter 
        #onmly add the letter if all match , else return prefix 
        firstword = strs[0]
        for i in range(len(strs[0])):
            for word in strs:
                if len(word) <= i or word[i] != firstword[i]:
                    return prefix
            prefix = prefix + firstword[i]
        return prefix  

        
