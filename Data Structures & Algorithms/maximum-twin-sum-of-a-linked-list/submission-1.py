# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        first_half_tail = slow
        

        current = slow.next
        new_current = None
        while current:                                    
            new_current2 = ListNode(val=current.val, next=new_current)
            new_current = new_current2

            current = current.next
        first_half_tail.next = None

        max_val = 0    
        
        second_head = new_current

        current = head
        new_current = second_head
        while current:
            max_val = max(max_val, current.val + new_current.val)
            current = current.next
            new_current = new_current.next        
        return max_val
        
