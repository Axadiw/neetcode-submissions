# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBST(root, rangeStart: float, rangeEnd: float) -> bool:
            if not root:
                return True
            
            current_satisfied = rangeStart < root.val and root.val < rangeEnd
            left_satisfied = isValidBST(root.left, rangeStart, root.val)
            right_satisfied = isValidBST(root.right, root.val, rangeEnd)

            return current_satisfied and left_satisfied and right_satisfied

        return isValidBST(root, float("-inf"), float("inf"))
        