from collections import deque
class RecentCounter:

    def __init__(self):
        self.times = deque()
        

    def ping(self, t: int) -> int:
        self.times.append(t)
        while self.times and self.times[0] < t - 3000: #remve
            self.times.popleft() #not in range
        return len(self.times) #everything removed thats not in range and we know that ping uses a strictly largert value if t
        #queue will never go ober size 3000
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)