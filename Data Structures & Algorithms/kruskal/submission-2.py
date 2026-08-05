class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.height = {}

        for i in range(n):
            self.parent[i] = i
            self.height[i] = 1
    
    def find(self, p1):
        while self.parent[self.parent[p1]] != self.parent[p1]:
            self.parent[p1] = self.parent[self.parent[p1]]
        
        return self.parent[p1]
    
    def union(self,p1 ,p2):
        p1 = self.find(p1)
        p2 = self.find(p2)

        if p1 == p2:
            return False
        
        if self.height[p1] > self.height[p2]:
            self.parent[p2] = p1
        elif self.height[p1] < self.height[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.height[p1] += 1        

        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        union = UnionFind(n)
        heap = []

        for u,v,w in edges:
            heapq.heappush(heap, (w,u,v))
        
        mst = []
        while heap:
            w,u,v = heapq.heappop(heap)
            if union.union(u,v):
                mst.append((w,u,v))
        
        if len(mst) != n-1:
            return -1

        mst_size = 0
        for w,u,v in mst:
            mst_size += w        
        return mst_size


