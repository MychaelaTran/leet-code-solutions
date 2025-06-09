from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        middle_use = False

        for word in list(count.keys()):
            rev = word[::-1]

            if word == rev:
                #word is stmmetruc 
                pairs = count[word] // 2
                length += pairs * 4 #one pair is 4 letters
                count[word] -= pairs * 2 #remove once used

                #use symmetric word for center, + 2
                if count[word] == 1 and not middle_use:
                    length += 2
                    middle_use = True
            #word is not its rev 
            elif word < rev: 
                pairs = min(count[word], count[rev])
                length += pairs * 4 #one pair is 4 leters 
                count[word] -= pairs
                count[rev] -= pairs

        return length
