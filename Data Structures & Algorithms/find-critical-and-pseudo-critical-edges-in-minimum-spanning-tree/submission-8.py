class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        numered_edges = []
        for i, edge in enumerate(edges):
            numered_edges.append((edge[0],edge[1],edge[2],i))

        def prim(new_edges,forced_edge):
            graph = {}

            for edge in new_edges:
                src,dst,w,i = edge
                if forced_edge and i == forced_edge[3]:
                    continue
                if src not in graph:
                    graph[src] = []
                if dst not in graph:
                    graph[dst] = []
                
                graph[src].append((w,dst,i))
                graph[dst].append((w,src,i))
            
            
            
            edges_used = set()
            heap = [(0,0,-1)]
            mst_size = 0
            visited = set()
            if forced_edge:                
                mst_size = forced_edge[2]
                heap = [
                    (0,forced_edge[0],forced_edge[3]),
                    (0,forced_edge[1],forced_edge[3])
                    ]
                # visited.add(forced_edge[0])
                # edges_used.add(forced_edge[3])
            # print(f"init heap: {heap} graph: {graph}")
                        
            while heap:                
                w1,p1,i1 = heapq.heappop(heap)
                # print(f"analyzing {i1} edge")                            
                if p1 in visited:
                    continue
                visited.add(p1)
                
                mst_size += w1
                if i1 >= 0:
                    edges_used.add(i1)
                    # print(f"add {i1} edge to used ones")                            
                # print(f"adding edges comint from point {p1}")  
                if p1 in graph:          
                    for edge in graph[p1]:
                        # print(f"adding edge {edge}")
                        heapq.heappush(heap,edge)
            
            # print(f"visited: {visited}")
            return (edges_used, mst_size if len(visited) == n else sys.maxsize)
        
        baseline_edges, baseline_weight = prim(numered_edges, None)
        # print(f"baseline_weight: {baseline_weight} baseline_edges: {baseline_edges}")
        
        crits = []
        noncrits = set()

        for i in range(len(numered_edges)):
            a = numered_edges[:i]+numered_edges[i+1:]
            e,w = prim(a,None)
            
            if w > baseline_weight:
                crits.append(i)

        # print(f"numered_edges: {numered_edges}")
        for i in range(len(numered_edges)):
        # for i in range(1):            
            e,w = prim(numered_edges,numered_edges[i])
            # print(f"detect noncrits for i {i}: e: {e} w: {w}")
            if w == baseline_weight:
                noncrits.add(i)
        
        for c in crits:
            if c in noncrits:
                noncrits.remove(c)
        
        return [crits,list(noncrits)]
            