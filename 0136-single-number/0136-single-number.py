class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR Of two of the same numbers is 0
        #XOR everything and the number remaining is iut (in binary)
        result = 0
        for num in nums:
            result ^= num


        return result


# When we do Xor opretion then dupliucate number cancel out each other and remain single number

# for exmple:- [ 4, 2, 1, 2, 1 ]

# 4 = 100, 2 = 010, 1 = 001

# 100 ^ 010 = 110

# 110 ^ 001 = 111

# 111 ^ 010 = 101

# 101 ^ 001 = 100

# 100 ^ 010 ^ 001 ^ 010 ^ 001 = 100
        