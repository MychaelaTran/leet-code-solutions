class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #engths need to match
        if len(word1) != len(word2):
            return False
        
        #same letter set
        if set(word1) != set(word2):
            return False

        #same frequences of any letters ie 3, 3, 5 also have 3, 5, 3,  NOT 3, 5, 5, 
        count1 = Counter(word1)
        count2 = Counter(word2)

        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True
