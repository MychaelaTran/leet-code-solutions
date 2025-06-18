from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque()
        rq = deque()
        n = len(senate)
        for i in range(n): 
            if senate[i] == "D":
                dq.append(i) #add its index of where we have dire
            else: 
                rq.append(i)
        #done two queues
        while dq and rq: 
            dire = dq.popleft()
            radiant = rq.popleft()
            if radiant < dire: #get rid of dire's rights
                rq.append(radiant + n)
            else: 
                dq.append(dire + n)
            

        if not dq: 
            return "Radiant"
        else: 
            return "Dire" 
            