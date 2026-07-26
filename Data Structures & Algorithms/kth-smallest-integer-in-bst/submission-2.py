# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def arrayed(root: Optional[TreeNode], k: int) -> List[int]:
            if not root.left and not root.right:
                return [root.val]
            
            
            l = arrayed(root.left, k) if root.left else []
            if len(l) + 1 >= k:
                return l + [root.val]
            return l + [root.val] + (arrayed(root.right, k) if root.right else [])

        return arrayed(root, k)[k-1]
        