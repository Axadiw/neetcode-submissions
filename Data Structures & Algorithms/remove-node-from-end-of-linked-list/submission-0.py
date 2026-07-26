# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head

        while current:
            current = current.next
            length +=1
        
        counter = 0

        i = length - n

        if i == 0:
            return head.next

        current = head
        prev = None
        while current:
            if counter == i:
                prev.next = current.next
                return head
            prev = current
            counter +=1
            current = current.next
            