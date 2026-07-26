# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        if head == None:
            return head

        while current != None:
            # print(f"reversing {current.val}")
            real_next = current.next            
            current.next = previous
            previous = current
            current = real_next

        return previous

        