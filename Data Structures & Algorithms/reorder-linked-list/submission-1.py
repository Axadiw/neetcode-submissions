# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        nodes = []
        while current:
            nodes.append(current)
            current = current.next            

        current = head
        counter = 0
        n = len(nodes)
        
        left = 0
        right = n-1
        
        while counter < n:
            if counter % 2 == 0:
                current.next = nodes[left]
                print(f"added left ({left})")
                left += 1
            else:
                current.next = nodes[right]
                print(f"added right ({right})")
                right -= 1
                
                
            counter += 1
            current = current.next
            print(f"left {left}, right {right}")
        
        if n % 2 == 0:
            current.next = nodes[right]
        current.next = None

        # current = head
        # vals = []
        # while current:
        #     vals.append(str(current.val))
        #     current = current.next
        # print(', '.join(vals))
    

        
        