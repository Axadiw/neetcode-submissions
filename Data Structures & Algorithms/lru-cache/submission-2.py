from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int
    next: Node
    prev: Node

class LRUCache:

    def __init__(self, capacity: int):
        self.max_len = capacity
        self.head = None
        self.tail = None        
        self.length = 0
        self.nodes_map = {}

    def get(self, key: int) -> int:
        if key in self.nodes_map:
            node = self.nodes_map[key]
            self.move_node_to_back(node)
            return node.val
        return -1

    def move_node_to_back(self, node: Node):        
        prev = node.prev
        next = node.next

        if not node.prev and not node.next:
            # single node in a list
            return

        if not next:
            # already on the back
            return            

        if not prev:
            #head
            new_head = node.next
            new_head.prev = None
            self.head = new_head
        
        if prev and next:
            # middle
            prev.next = next
            next.prev = prev
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node     
        node.next = None           

    def put(self, key: int, value: int) -> None:
        if key in self.nodes_map:
            self.nodes_map[key].val = value
            self.move_node_to_back(self.nodes_map[key])
            return
        
        new_node = Node(key=key, val=value, next=None, prev=None)
        if self.length < self.max_len:
            if self.length == 0:
                self.head = new_node
                            
            if self.tail:
                new_node.prev = self.tail
                self.tail.next = new_node
            self.tail = new_node

            self.length += 1
        else:
            del self.nodes_map[self.head.key]

            if self.max_len == 1:
                self.head = new_node
            elif self.head and self.head.next:                
                second_item = self.head.next
                second_item.prev = None
                self.head = second_item

            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.nodes_map[key] = new_node
        
        
