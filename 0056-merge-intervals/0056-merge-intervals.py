class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals!
        intervals.sort(key=lambda x: x[0])
        merged = []
        print(intervals)
        curr = intervals[0]
        end = curr[1]
        for interval in intervals: 
            if interval[0] <= end: #overlap
                end = max(interval[1], curr[1])
                curr[1] = end
            else: #no overalap
                merged.append([curr[0], end])
                curr = interval
                end = curr[1]
                
        merged.append([curr[0], end])
        
        return merged