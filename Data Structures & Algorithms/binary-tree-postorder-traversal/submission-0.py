# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret_val = []
        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal ret_val
            if not root:
                return
                        
            dfs(root.left)
            dfs(root.right)
            ret_val.append(root.val)

        dfs(root)
        return ret_val