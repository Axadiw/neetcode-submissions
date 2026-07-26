class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        # print(graph)
        for item in graph.items():
            visited = set()
            queue = deque()
            # print(f"looking for cycles starting from {item[0]}")

            def isThereCycle(node, visited):
                if node in visited:
                    return True
                
                visited.add(node)
                for next in graph[node]:
                    if isThereCycle(next, visited):
                        return True
                visited.remove(node)

                return False

            if isThereCycle(item[0],set()):
                return False
                        
        return True
        