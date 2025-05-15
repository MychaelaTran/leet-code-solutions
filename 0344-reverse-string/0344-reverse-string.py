class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        indexNums = len(s) - 1
        i = 0
        j = indexNums
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s        