class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0
        
        points = [(x[0],x[1]) for x in points]
        
        visited = set()
        ret = []

        def manhattan(p1,p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

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
                
                heapq.heappush(heap, (manhattan(point, p1), point))
        
        return sum(ret)