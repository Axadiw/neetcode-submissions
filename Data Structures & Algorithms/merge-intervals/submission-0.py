class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        
        sintervals = sorted(intervals, key=lambda x: x[0])
        ret = [sintervals[0]]            
        i = 1
        
        while i<n:
            if sintervals[i][0] <= ret[-1][1]:
                ret[-1] = [min(sintervals[i][0],ret[-1][0]),max(sintervals[i][1],ret[-1][1])]
            else:
                ret.append(sintervals[i])
            i+=1
        
        return ret
        
        