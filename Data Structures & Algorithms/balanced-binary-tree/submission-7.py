# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> tuple[int, bool]:
            if not root:
                # print(f"came to {root.val if root else 'None'}. last node, returning height 0")
                return 0, True
            if not root.left and not root.right:
                # print(f"came to {root.val if root else 'None'}. last node, returning height 0")
                return 1, True
            
            left_height = 0
            right_height = 0
            if root.left:
                # print(f"left of {root.val} is {root.left.val}")
                left_height += height(root.left)[0]
            if root.right:
                # print(f"right of {root.val} is {root.right.val}")
                right_height += height(root.right)[0]
            
            # print(f"came to {root.val }. Left height  {left_height}, Right height  {right_height}")
            return max(left_height, right_height) +1, abs(left_height - right_height) <= 1

        if not root:
            return True

        left_height, left_is_balanced = height(root.left)
        right_height, right_is_balanced = height(root.right)
        current_balanced = abs(left_height - right_height) <= 1

        return current_balanced and left_is_balanced and right_is_balanced
