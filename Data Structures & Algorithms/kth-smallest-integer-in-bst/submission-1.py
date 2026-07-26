# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def arrayed(root: Optional[TreeNode]) -> List[int]:
            if not root.left and not root.right:
                return [root.val]
            
            
            l = arrayed(root.left) if root.left else []
            p = arrayed(root.right) if root.right else []
            return l + [root.val] + p

        return arrayed(root)[k-1]
        