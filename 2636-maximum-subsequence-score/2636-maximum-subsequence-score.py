import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        pairs.sort(reverse=True) #sort by descending order of nums2
        
        maxx = 0
        curr = 0
        heap = []

        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            curr += n1

            if len(heap) > k: #remove smallest number from heap (smallest n1 on heap)
                curr -= heapq.heappop(heap)

            if len(heap) == k: 
                maxx = max(curr * n2, maxx) #since h(n2,n1) pauirs in descreasing order, curr n2 will be minimum

        return maxx