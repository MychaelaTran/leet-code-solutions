class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals!
        intervals.sort(key=lambda x: x[0])

        merged = []
        
        for interval in intervals:
            #if the list of merged intervals is empty 
            #or if the curr interval doesn't overlap with prev, 
            # simply append it.
            fst_elm = interval[0]
            if len(merged) == 0 or fst_elm > merged[-1][1]:
                merged.append(interval)
            else: #overlap in this case 
                #merge by taking the max end time from the overlap start times 
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged