class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        sintervals = sorted(intervals, key=lambda x: x[0])
        i = 1

        while i < len(sintervals):
            if sintervals[i][0] < sintervals[i-1][1]:
                i_to_remove = i if (sintervals[i][1]) > (sintervals[i-1][1]) else i-1
                sintervals.pop(i_to_remove)                
            else:
                i+=1
        
        return n - len(sintervals)