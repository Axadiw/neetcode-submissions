# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def is_path_smaller(root: TreeNode, path: List[int]) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                condition_met = len([x for x in path if x > root.val]) == 0
                return 1 if condition_met else 0
            
            condition_met = len([x for x in path if x > root.val]) == 0
            nodes_count = 1 if condition_met else 0
            if root.left:
                nodes_count += is_path_smaller(root.left, path + [root.val])
            if root.right:
                nodes_count += is_path_smaller(root.right, path + [root.val])

            return nodes_count
        
        return is_path_smaller(root, [])
        