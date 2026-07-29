class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(1,n+1):
            graph[i] = []
        
        for u,v,t in times:
            graph[u].append((t,v))
        
        shortest = {}
        heap = [(0,k)]

        while heap:
            w1,n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for w2,n2 in graph[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, (w1+w2,n2))
        for i in range(1,n+1):
            if i not in shortest:
                return -1
        
        return max(shortest.values())