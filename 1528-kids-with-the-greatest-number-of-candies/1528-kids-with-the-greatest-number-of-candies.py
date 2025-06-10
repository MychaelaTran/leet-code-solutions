class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr_max = max(candies)
        f = lambda x: x + extraCandies >= curr_max
        return list(map(f, candies))