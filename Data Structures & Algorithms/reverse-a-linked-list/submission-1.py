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

        while True:
            # print(f"reversing {current.val}")
            should_finish = False
            real_next = current.next
            if current.next == None:
                should_finish = True
            
            current.next = previous
            if should_finish:
                break

            previous = current
            current = real_next

        return current

        