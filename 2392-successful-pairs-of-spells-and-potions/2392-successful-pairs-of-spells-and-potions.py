class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = [0 for _ in range(len(spells))]
        
        #sort potions and find when succesful and then we know all rest potions will pass
        potions = sorted(potions)
        
        for spell in range(len(spells)): 
            good = 0
            high = len(potions) -1
            low = 0
            temp = 1000000000000
            #binary search to always get lowest if there are duplicates 
            while low <= high: 
                mid = (high + low)//2 
                if spells[spell] * potions[mid] >= success:
                    temp = mid
                    high = mid - 1
                else:
                    low = mid + 1


            if temp != 1000000000000: 
                good = len(potions) - temp
            ans[spell] = good
       
        return ans


            

        