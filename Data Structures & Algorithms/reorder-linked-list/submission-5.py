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

        print(f"first_half_tail {first_half_tail.val}")

        second_half_tail = slow.next
        first_half_tail.next = None
        print(f"second_half_tail {second_half_tail.val}")

        current  = second_half_tail
        prev = None
        while current:
            next, current.next, prev = current.next, prev, current
            current = next

        second_half_head = prev

        items1 = []
        items2 = []

        current = head
        while current:
            items1.append(str(current.val))
            current = current.next

        current = second_half_head
        while current:
            items2.append(str(current.val))
            current = current.next

         
        print(f"second_half_head {second_half_head.val}")
        print(f"first half = {", ".join(items1)}")
        print(f"second half = {", ".join(items2)}")

        ret_current = head
        
        current = head.next
        current2 = second_half_head

        counter = 0
        while current or current2:
            if counter % 2 == 0:
                ret_current.next = current2
                print(f"index {counter} adding {current2.val}")
                current2 = current2.next
            else:
                ret_current.next = current
                print(f"index {counter} adding {current.val}")
                current = current.next
            
            ret_current = ret_current.next
            counter += 1
        print('finn')


        