from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        total_triplets = 0
        pair_sum_freq = Counter()

        #pretend third element k, so cam look at all element before 
        for third_index in range(len(arr)):
            third = arr[third_index]

            #how many (first, second) pairs we've seen so far that sum (target - third)
            complement = target - third
            total_triplets += pair_sum_freq[complement]

            # Now update the pair_sum_freq map with all pairs (first, third)
            for first_index in range(third_index):
                first = arr[first_index]
                pair_sum = first + third
                pair_sum_freq[pair_sum] += 1

        return total_triplets % MOD
