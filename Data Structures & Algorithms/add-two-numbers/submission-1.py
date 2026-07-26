# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = l1
        current2 = l2
        acc = 0
        retval = 0
        return_head = ListNode()
        return_current = return_head
        while current or current2:
            val1 = current.val if current else 0
            val2 = current2.val if current2 else 0
            acc += val1 + val2

            return_current.next = ListNode(val=acc % 10)
            return_current = return_current.next
            acc = acc // 10 

            tail = current

            if current:
                current = current.next
            
            if current2:
                current2 = current2.next

        while acc > 0:
            new_node = ListNode(val=acc % 10)
            return_current.next = new_node
            return_current = new_node
            acc = acc // 10
        
        return return_head.next