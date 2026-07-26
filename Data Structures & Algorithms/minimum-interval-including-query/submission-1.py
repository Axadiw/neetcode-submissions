# brute force

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sintervals = sorted(intervals, key=lambda x: x[0])
        for idx, query in enumerate(queries):
            shortest = sys.maxsize
            for interval in sintervals:
                if interval[0] > query:
                    break
                
                if interval[0] <= query and interval[1] >= query:
                    # intersection
                    # print(f"for query {query} I'm assiming {interval} is shortest (length: {interval[1] - interval[0]+1})")
                    shortest = min(shortest, interval[1] - interval[0] +1)
            
            queries[idx] = shortest if shortest != sys.maxsize else -1
        
        return queries
