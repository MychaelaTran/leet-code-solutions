class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = Counter(arr)

        #sort by abs so we match nums properly 
        for num in sorted(freq.keys(), key=abs):
            double = num * 2

            if freq[double] < freq[num]:
                #not enough doubles to pair with our numebr 
                return False
            
            #subtract whjat we used
            freq[double] -= freq[num]
            # freq[num] is now used up, implicitly treated as 0

        return True