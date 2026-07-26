# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def print_list(head: Optional[ListNode]):
            vals = []
            current = head
            while current:
                vals.append(str(current.val))
                current = current.next
            
            print(", ".join(vals))


        def reverse_list(head: Optional[ListNode], tail: Optional[ListNode]):
            current = head
            tail.next = None
            prev = None
            while current:
                next = current.next   
                current.next = prev
                prev = current
                current = next

        
        left = right = head
        counter = 0
        tmp_head = ListNode(val=-1, next=head)


        while right and right.next:            
            if counter == k-1:
                break
            right = right.next                
            counter += 1

        prev = tmp_head
        print(f'start counter {counter} left {left.val} right {right.val}')
        while right:
            # print(f"counter {counter}")
            counter += 1                
            if counter >= k:
                next = right.next
                # print(f'counter {counter} left {left.val} right {right.val} next {next.val} prev {prev.val}')
                reverse_list(left, right)
                # print_list(right)
                left.next = next
                prev.next = right
                counter = 0
                tmp = left
                left = right
                right = tmp
                # print(f'after reversing left {left.val} right {right.val} right.next {right.next.val}')
            
            prev = left    
            left = left.next
            right = right.next

        return tmp_head.next

        