# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current != None:
            # print(f"reversing {current.val}")
            # real_next = current.next            
            # current.next = previous
            # previous = current
            # current = real_next

            current.next, current, previous = previous, current.next, current

        return previous

        