class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for from_i, to_i, price_i in flights:
            graph[from_i].append((price_i,to_i))
        
        heap = [(0,src,0,set())]
        min_far = sys.maxsize
        while heap:
            w1,p1,far,visited = heapq.heappop(heap)
            if p1 in visited:
                continue

            if far > k+1:
                continue

            if p1 == dst:
                return w1
                continue            
            
                        
            visited.add(p1)
            for w2,p2 in graph[p1]:
                heapq.heappush(heap, (w1+w2,p2,far+1,visited.copy()))
        
        return min_far if min_far < sys.maxsize else -1

        