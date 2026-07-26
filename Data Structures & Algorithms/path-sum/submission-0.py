# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def pathSum(root: Optional[TreeNode], targetSum: int, sumSoFar: int) -> bool:
            if not root:
                return False

            if not root.left and not root.right:
                # print(f"came to an end {sumSoFar}, left:{root.left} right: {root.right}")
                return sumSoFar + root.val == targetSum

            # print(f"val: {root.val}, sumsofar: {sumSoFar} left:{root.left} right:{root.right}")
            val1 = pathSum(root.left, targetSum, sumSoFar + root.val)
            val2 = pathSum(root.right, targetSum, sumSoFar + root.val)  
            # print(f"val1: {val1} val2: {val2} or: {val1 or val2}")
            return val1 or val2
        
        return pathSum(root, targetSum, 0)

        