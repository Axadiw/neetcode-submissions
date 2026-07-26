# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast.next != None and fast.next.next != None and slow.next != None:
            slow, fast = slow.next, fast.next.next

        return slow if fast.next == None else slow.next
        