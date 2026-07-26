# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def areTreesSame(self, root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root or not root2:
            return not root and not root2

        if not root.left and not root.right:
            return root2.val == root.val and not root2.left and not root2.right

        if root.left and not self.areTreesSame(root.left,root2.left):
            return False
        if root.right and not self.areTreesSame(root.right,root2.right):
            return False

        return root.val == root2.val

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return self.areTreesSame(root, subRoot)
        
        if root.left:
            if self.areTreesSame(root.left, subRoot):
                return True
            return self.isSubtree(root.left, subRoot)
    
        if root.right:
            if self.areTreesSame(root.right, subRoot):
                return True
            return self.isSubtree(root.right, subRoot)
        
        return self.areTreesSame(root, subRoot)
        