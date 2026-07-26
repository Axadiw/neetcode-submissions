# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        nodes = lists

        def are_all_nodes_none(nodes):
            for node in nodes:
                if node:
                    return False
            return True
        
        def get_smallest_node(nodes):
            smallest_node = None
            smallest_node_index = -1
            for idx, node in enumerate(nodes):
                if node and (not smallest_node or node.val < smallest_node.val):
                    smallest_node = node
                    smallest_node_index = idx
            nodes[smallest_node_index] = nodes[smallest_node_index].next
            return smallest_node

        while not are_all_nodes_none(nodes):
            smallest_node = get_smallest_node(nodes)
            smallest_node.next = None
            tail.next = smallest_node
            tail = smallest_node


        return dummy.next