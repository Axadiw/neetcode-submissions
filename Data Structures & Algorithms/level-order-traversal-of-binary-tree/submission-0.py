# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        fifo = deque()

        if root:
            fifo.append(root)

        ret_val = []
        while len(fifo) > 0:
            level_array = []
            for i in range(len(fifo)):
                item = fifo.popleft()
                level_array.append(item.val)
                # print(f"val: {item.val} level: {level}")
                if item.left:
                    fifo.append(item.left)
                if item.right:
                    fifo.append(item.right)
            
            ret_val.append(level_array)
        return ret_val
        