class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spots = len(flowerbed)
        for i in range(len(flowerbed)): 
            if flowerbed[i] == 1: 
                continue
            else: 
                if n == 0: 
                    return True

                if i == 0 and len(flowerbed) > 1: 
                    if flowerbed[i + 1 ] == 0: 
                        flowerbed[i] = 1
                        n -= 1
                        continue
                
                if i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0: 
                        n -= 1
                        continue

                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0: 
                    flowerbed[i] = 1
                    n -= 1
        
        if n == 0: 
            return True
        else: 
            return False
            
        
        