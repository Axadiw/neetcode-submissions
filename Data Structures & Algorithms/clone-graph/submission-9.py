"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        nnodes = {}
        visited = {}
        queue = deque()
        queue.append(node)
        
        while queue:
            for _ in range(len(queue)):
                element = queue.popleft()

                if element.val in visited:
                    continue
                else:
                    new = nnodes[element.val] if element.val in nnodes else Node(val=element.val)
                    nnodes[element.val] = new
                    visited[element.val] = new
                    for n in element.neighbors:
                        newer = nnodes[n.val] if n.val in nnodes else Node(val=n.val)
                        nnodes[n.val] = newer
                        new.neighbors.append(newer)
                        queue.append(n)                                

        return visited[node.val]
        