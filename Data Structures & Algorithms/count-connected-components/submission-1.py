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
            if not i in colored:
                counter += 1
                for node in dfs(i,set()):
                    colored[node] = counter
        
        return counter

            
        