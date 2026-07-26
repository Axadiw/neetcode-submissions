# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        return_value = float("-inf")
        def max_road(root: Optional[TreeNode]) -> int:
            nonlocal return_value
            if not root:
                return float("-inf")
            
            # print(f"{root.val} L: {root.left.val if root.left else '-'} R: {root.right.val if root.right else '-'}")
            
            max_path_left = max_road(root.left) if root.left else -sys.maxsize
            max_path_right = max_road(root.right) if root.right else -sys.maxsize
            # max_path = max(max(max(max_path_left, max_path_right),max_path_left + max_path_right + root.val), root.val)
            max_path = max(max_path_left,max_path_right,root.val,max_path_right+root.val+max_path_left, max_path_left+root.val, max_path_right +root.val)
            # print(f"root.val {root.val} max_path_left {max_path_left} max_path_right {max_path_right} max_path {max_path}")
            return_value = max(max_path, return_value)

            # print(f"{root.val} will return {max(root.val + max_path_right, root.val + max_path_left, root.val)}")
            return max(root.val + max_path_right, root.val + max_path_left, root.val)
        max_road(root)

        return return_value