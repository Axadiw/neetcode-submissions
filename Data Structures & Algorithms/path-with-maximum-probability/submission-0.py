class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for i,val in enumerate(edges):
            graph[val[0]].append((succProb[i],val[1]))
            graph[val[1]].append((succProb[i],val[0]))

        heap = [(1,start_node)]
        shortest = {}
        
        while heap:
            w1,n1 = heapq.heappop(heap)
            print(f"analuzing w1 {w1} n1 {n1}")
            if n1 in shortest:
                continue
            
            if n1 == end_node:
                return -w1
            
            shortest[n1] = w1

            for w2,n2 in graph[n1]:
                heapq.heappush(heap, (-abs(w1*w2),n2))
            
        return 0

        