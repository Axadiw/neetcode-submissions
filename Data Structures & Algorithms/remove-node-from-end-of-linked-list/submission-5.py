# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head

        if not head.next:
            return None

        for i in range(0,n):
            right = right.next

        if not right:
            return head.next            
        
        print(f'left {left.val}')
        print(f'right {right.val}')
        while right:
            if right.next:
                right = right.next
                left = left.next
            else:
                left.next = left.next.next
                return head
        
        