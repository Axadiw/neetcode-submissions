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
                left += 1
            else:
                current.next = nodes[right]
                right -= 1
                
                
            counter += 1
            current = current.next
        
        current.next = None

        
        