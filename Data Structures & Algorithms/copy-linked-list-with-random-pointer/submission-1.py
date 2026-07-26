"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head        
        new_head = None
        nodes_map = {}
        prev = None

        while current:
            new_node = Node(x=current.val)

            if prev:
                prev.next = new_node

            if current == head:
                new_head = new_node

            prev = new_node
            nodes_map[current] = new_node
            current = current.next

        current = head        
        new_current = new_head

        while current:
            if current.random and current.random in nodes_map :
                new_current.random = nodes_map[current.random]

            current = current.next
            new_current = new_current.next

        return new_head
        