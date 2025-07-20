from heapq import heappop, heappush, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #make into a mihn heap using the heap library and pop n-k
        length = len(nums)
        heapify(nums) #heapufy creates a min heap 
        pop_num = length - k
        for _ in range(pop_num ):
            heappop(nums)

        return heappop(nums)
        #O(n + klogn)
        