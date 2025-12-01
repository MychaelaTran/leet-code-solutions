class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort start times
        intervals.sort(key=lambda x: x[0])

        #use a stack to do merges 
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            last_merged_interval = ans[-1] 

            #check overalp 
            if curr_interval[0] <= last_merged_interval[1]:
                #need to merge [1,12] [2,10]
                last_merged_interval[1] = max(last_merged_interval[1], curr_interval[1])
            else:
                ans.append(curr_interval)
        
        return ans