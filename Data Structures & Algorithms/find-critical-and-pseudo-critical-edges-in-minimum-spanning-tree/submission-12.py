class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.heights = {}

        for i in range(n):
            self.parents[i] = i
            self.heights[i] = 1
    
    def find(self,n):                    
        if n != self.parents[n]:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
    
    def union(self, p1,p2):
        parent_1 = self.find(p1)
        parent_2 = self.find(p2)

        if parent_1 == parent_2:
            return False
        
        if self.heights[parent_1] > self.heights[parent_2]:
            self.parents[parent_2] = parent_1
        elif self.heights[parent_1] < self.heights[parent_2]:
            self.parents[parent_1] = parent_2

        else:
            self.heights[parent_2] += self.heights[self.parents[p1]]
            self.parents[parent_1] = parent_2            
    
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def kruskal_size(graph_n, graph_edges, forced_edge):
            # print(f"kruskal_size asked. edges: {graph_edges}")
            if graph_n == 0:
                return 0

            finder = UnionFind(n)
            
            heap = []
            size = 0
            edges_added = 0
            if forced_edge:
                size += forced_edge[2]
                edges_added = 1
                finder.union(forced_edge[0],forced_edge[1])
            for u,v,w in graph_edges:
                heapq.heappush(heap, (w,u,v))
            
            while heap:
                w,u,v = heapq.heappop(heap)

                if finder.union(u,v):
                    # print(f"added edge {u} - {v} w: {w}")
                    size += w
                    edges_added += 1
            
            return size if edges_added == graph_n-1 else -1
        
        baseline_size = kruskal_size(n,edges, None)

        print(f"baseline_size: {baseline_size}")

        crits = set()
        non_crits = []
        for i in range(len(edges)):            
            size = kruskal_size(n, edges[:i] + edges[i+1:], None) 
            print(f"crits - i: {i} size: {size}")
            if size > baseline_size or size < 0:
                crits.add(i)
        
        for i in range(len(edges)):            
            size = kruskal_size(n, edges[:i] + edges[i+1:], edges[i]) 
            print(f"noncrits -  i: {i} size: {size}")
            if size == baseline_size and i not in crits and size >= 0:
                non_crits.append(i)
        

        return [list(crits),non_crits]
            
            

        


        