# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_val = 0
        def longest_branch(root: Optional[TreeNode]) -> int:
            nonlocal max_val
            if not root.left and not root.right:
                return 0
            
            left_height = right_height = 0
            if root.left:
                left_height += longest_branch(root.left) + 1
        
            if root.right:
                right_height += longest_branch(root.right) + 1
            
            max_val = max(max_val,left_height + right_height)
            return max(left_height, right_height)
            



        if not root:
            return 0
        
        longest_branch(root)
        return max_val
        
        
        

        
