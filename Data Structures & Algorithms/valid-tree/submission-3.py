class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}

        if n == 0:
            return False
        

        for i in range(n):
            graph[i] = set()
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        
        seen = set()
        def dfs(i,visited, prev):
            print(f'analyzing {i}')

            seen.add(i)
            if i in visited:
                print(f'{i} already seen')
                return False
            
            if len(graph[i]) == 0 and n>1:
                print(f'{i} is lonely node')
                return False
            
            for next in graph[i]:
                visited.add(i)
                if next != prev and not dfs(next,visited,i):
                    return False
                visited.remove(i)
            
            return True
        
        cycle_not_found = dfs(0,set(),None)
        return cycle_not_found and len(seen) == n
        