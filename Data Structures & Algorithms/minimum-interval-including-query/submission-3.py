class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sintervals = sorted(intervals, key=lambda x: x[0])
        squeries = sorted(queries)
        nq = len(queries)
        responses = {}

        def find(i):
            L = 0
            R = nq-1

            while L < R:
                mid = (R - L) // 2 + L

                if squeries[mid] >= i:
                    R = mid
                else:
                    L = mid + 1
            
            return L

        print(f"squeries: {squeries}")

        for interval in sintervals:
            begin = find(interval[0])
            end = find(interval[1])

            print(f"for interval {interval} queries have indexes {begin}+ and {end}- from squeries")


            if end >= begin:
                for i in range(begin,end+1):
                    if squeries[i] >= interval[0] and squeries[i] <= interval[1]:
                        length = interval[1]-interval[0] + 1
                        if squeries[i] in responses:
                            responses[squeries[i]] = min(responses[squeries[i]], length)
                        else:
                            responses[squeries[i]] = length
        
        result = [-1] * len(queries)
        for i in range(len(queries)):
            if queries[i] in responses:
                result[i] = responses[queries[i]]
        
        return result

        