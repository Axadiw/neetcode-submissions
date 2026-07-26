class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = set()
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        def dfs(node, visited):
            if node in visited:
                return

            visited.add(node)
            for connected_node in graph[node]:
                dfs(connected_node, visited)
            
            return visited
            

        colored = {}
        counter = 0
        for i in range(n):
            found_new_node = False            
            for node in dfs(i,set()):
                if not node in colored and not found_new_node:
                    counter += 1
                    found_new_node = True

                colored[node] = counter
        
        return counter

            
        