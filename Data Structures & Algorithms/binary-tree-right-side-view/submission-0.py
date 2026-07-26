# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        fifo = deque()

        if not root:
            return []
        
        ret_val = []
        fifo.append(root)

        while len(fifo) > 0:
            for i in range(len(fifo)):
                item = fifo.popleft()

                if i == 0:
                    ret_val.append(item.val)

                if item.right:
                    fifo.append(item.right)
                
                if item.left:
                    fifo.append(item.left)

        return ret_val
        