class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_count = [0] * 60
        count = 0

        for t in time:
            rem = t % 60
            complement = (60 - rem) % 60
            count += remainder_count[complement] #make sure we are only adding it if it came AFFTER because waht is in remainder is what came previosuly 
            remainder_count[rem] += 1

        return count
