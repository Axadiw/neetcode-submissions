class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        
        points = [(x[0],x[1]) for x in points]
        
        visited = set()
        ret = []


        cache = {}        
        def manhattan(p1,p2):
            if (p1,p2) in cache:
                return cache[(p1,p2)]
            val = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            cache[(p1,p2)] = val
            cache[(p2,p1)] = val
            return val

        heap = [(0,points[0])]

        while heap:
            w1, p1 = heapq.heappop(heap)
            if p1 in visited:
                continue
            
            visited.add(p1)
            ret.append(w1)

            for point in points:
                if point[0] == p1[0] and point[1] == p1[1]:
                    continue
                
                if point in visited:
                    continue
                
                heapq.heappush(heap, (manhattan(point, p1), point))
        
        return sum(ret)