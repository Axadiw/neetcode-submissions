from dataclasses import dataclass
from typing import Optional

@dataclass
class LinkedListNode:
    val: int
    prev: Optional[LinkedListNode]
    next: Optional[LinkedListNode]

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def print(self):
        current = self.head
        index = 0 
        values = []
        while current != None:
            values.append(f"{index}: {current.val}")
            current = current.next
            index += 1

        # print(', '.join(values))

    def length(self) -> int:
        current = self.head
        index = 0 
        while current != None:
            current = current.next
            index += 1

        return index

    def get_node(self, index: int) -> int:
        self.print()

        if self.head == None:
            # print(f"[get] head is empty")
            return None
        
        current = 0
        current_node = self.head
        while current <= index:
            # print(f"[get @ {index}] current {current_node}")
            if current == index:
                # print(f"[get @ {index}] returning {current_node}")
                return current_node

            current_node = current_node.next

            if current_node == None:
                print(f"[get @ {index}] eached an end - returning None")
                return None
            current += 1

    def get(self, index: int) -> int:
        node = self.get_node(index)

        return node.val if node != None else -1


    def addAtHead(self, val: int) -> None:
        new_value = LinkedListNode(val=val, prev=None, next=self.head)
        if self.head:            
            self.head.prev = new_value
            self.head = new_value
        else:
            self.tail = new_value
            self.head = new_value
        self.print()
        
        # print(f"[addAtHead] head {self.head}")
        # print(f"[addAtHead] tail {self.tail}")

    def addAtTail(self, val: int) -> None:
        new_value = LinkedListNode(val=val, prev=self.tail, next=None)
        if self.tail:            
            self.tail.next = new_value
            self.tail = new_value
        else:
            self.tail = new_value
            self.head = new_value
        self.print()
        # print(f"[addAtTail] head {self.head}")
        # print(f"[addAtTail] tail {self.tail}")

    def addAtIndex(self, index: int, val: int) -> None:
        length = self.length()
        # print(f"[addAtIndex] length = {length}")
        if index == length:
            self.addAtTail(val)
            return

        node = self.get_node(index)        

        if node == None:
            # print(f"[addAtIndex] got none - not adding a value at index {index}")
            return

        previous = node.prev
        new_value = LinkedListNode(val=val, prev=node.prev, next=node)
        node.prev = new_value
        previous.next = new_value

        self.print()

    def deleteAtIndex(self, index: int) -> None:
        node = self.get_node(index)

        if node == None:
            return
        
        if node.prev == None and node.next == None:
            self.head = None
            self.tail = None
            return
        
        if node.prev == None:
            self.head = node.next
            return
        
        if node.next == None:
            previous = node.prev
            previous.next = None
            self.tail = previous
            return
        
        previous = node.prev
        next = node.next
        previous.next = next
        next.prev = previous


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)