class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")
        s = list(s)  #can;t mutate strings...
        left = 0
        right = len(s) - 1


        #TWO POINTER TECHNIQUE
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
    
            #swap the vowels once left and right ptr reach a vowel 
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s) 
