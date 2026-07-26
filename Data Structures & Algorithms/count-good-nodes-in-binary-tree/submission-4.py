# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def is_path_smaller(root: TreeNode, max_so_far: int) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 1 if root.val >= max_so_far else 0
            
            nodes_count = 1 if root.val >= max_so_far else 0
            if root.left:
                nodes_count += is_path_smaller(root.left, max(max_so_far, root.val))
            if root.right:
                nodes_count += is_path_smaller(root.right, max(max_so_far, root.val))

            return nodes_count
        
        return is_path_smaller(root, -101)
        