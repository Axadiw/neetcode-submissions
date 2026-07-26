# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        if not head.next:
            return

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        first_half_tail = slow

        second_half_tail = slow.next
        first_half_tail.next = None

        current  = second_half_tail
        prev = None
        while current:
            next, current.next, prev = current.next, prev, current
            current = next

        second_half_head = prev
        ret_current = head

        current = head
        current2 = second_half_head

        while current2:
            next1 = current.next
            next2 = current2.next

            current.next = current2
            current2.next = next1

            current = next1
            current2 = next2
        


        