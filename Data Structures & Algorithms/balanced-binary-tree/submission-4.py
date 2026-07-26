# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                print(f"came to {root.val if root else 'None'}. last node, returning height 0")
                return 0
            if not root.left and not root.right:
                print(f"came to {root.val if root else 'None'}. last node, returning height 0")
                return 1
            
            left_height = 0
            right_height = 0
            if root.left:
                print(f"left of {root.val} is {root.left.val}")
                left_height += height(root.left)
            if root.right:
                print(f"right of {root.val} is {root.right.val}")
                right_height += height(root.right)
            
            print(f"came to {root.val }. Left height  {left_height}, Right height  {right_height}")
            return max(left_height, right_height) +1

        if not root:
            return True

        current_balanced = abs(height(root.left) - height(root.right)) <= 1
        left_balanced = self.isBalanced(root.left)
        right_balanced = self.isBalanced(root.right)


        return current_balanced and left_balanced and right_balanced
