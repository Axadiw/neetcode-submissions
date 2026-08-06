class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        
        if len(prerequisites) == 0:
            return [False] * len(queries)
            
        for pre,post in prerequisites:
            graph[pre].append(post)

        def traversal(node, visited, ret):        
            if node in visited:
                return
            
            visited.add(node)
            
            for child in graph[node]:
                traversal(child, visited, ret)
                
            ret.add(node)

        paths = {}

        for i in range(numCourses):
            single_topology = set()
            traversal(i, set(), single_topology)
            paths[i] = single_topology        
        
        return [x[1] in paths[x[0]] for x in queries]
