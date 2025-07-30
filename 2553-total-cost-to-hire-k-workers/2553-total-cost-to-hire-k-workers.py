class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        total = 0 

        #add to heap ecostsach round the candidates sorted by costs
        #add from front of candiates
        for i in range(candidates): 
            heapq.heappush(heap, (costs[i], i))
            front_end = i
    
        #do this from the back end now (instead of doing for loop can find where back starts)
        back_start = max(len(costs)- candidates, front_end + 1)
        for j in range(back_start, len(costs)): 
            heapq.heappush(heap, (costs[j], j))
        
        while k > 0: 
            cost, worker = heapq.heappop(heap)
            total += cost
            k-= 1

            #expand heap from either front end or back ene
            if front_end < back_start -1: #not evberything in costs added , so have to add
                if worker <= front_end: #add +1 from front end
                    front_end += 1
                    heapq.heappush(heap, (costs[front_end], front_end))
                else: 
                    back_start -= 1
                    heapq.heappush(heap, (costs[back_start], back_start))
            
     
        return total



#choose worker with lowest cost from eother the first candiates workers or the last , break ties bty smallest index  
        