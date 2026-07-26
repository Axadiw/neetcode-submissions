# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        retListCurrent = None
        retListHead = None

        if current1 == None:
            return current2
        if current2 == None:
            return current1
        
        if current1.val < current2.val:
            retListHead = current1
            current1 = current1.next
        else:
            retListHead = current2
            current2 = current2.next

        retListCurrent = retListHead


        while current1 != None or current2 != None:
            if current2 == None or (current1 != None and current1.val < current2.val):                                
                retListCurrent.next = current1
                retListCurrent = current1
                current1 = current1.next
            else:                
                retListCurrent.next = current2
                retListCurrent = current2
                current2 = current2.next
            
        
        return retListHead 
            
        