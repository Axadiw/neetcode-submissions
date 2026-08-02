class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        
        points = [(x[0],x[1]) for x in points]
        
        visited = set()
        ret = []

        def manhattan(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        distances = {}
        for p1 in points:
            distances[p1] = {}
            for p2 in points:
                distances[p1][p2] = manhattan(p1,p2)

        heap = [(0,points[0])]

        while heap:
            w1, p1 = heapq.heappop(heap)
            if p1 in visited:
                continue
            
            visited.add(p1)
            ret.append(w1)

            for point in points:
                if point in visited or point == p1:
                    continue                
                
                heapq.heappush(heap, (distances[point][p1], point))
        
        return sum(ret)