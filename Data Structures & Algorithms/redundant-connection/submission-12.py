class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes_len = len(edges)
        

        for i in range(len(edges)-1,-1,-1):
            new_list = edges[:i] + edges[i+1:]
            graph = {}
            
            def visited_len(i, visited,prev):
                if i in visited:
                    return -1

                if len(graph[i]) == 0:
                    return 1
                
                for node in graph[i]:
                    visited.add(i)
                    if node != prev and visited_len(node,visited,i) < 0:
                        return -1
                
                return len(visited)
            for n in range(1,nodes_len+1):
                graph[n] = set()
            for edge in new_list:
                graph[edge[0]].add(edge[1])
                graph[edge[1]].add(edge[0])
            if visited_len(1,set(),None) == n:
                return edges[i]
            
                
                
            

        