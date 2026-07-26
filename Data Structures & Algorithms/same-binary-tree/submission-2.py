# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def root_repr(root: Optional[TreeNode]) -> str:
            if not root:
                return ''
            
            return f"{root.val}{'L' if root.left else ''}{'R' if root.right else ''}"

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p or not q) or (not p.left and not p.right) or (not q.left and not q.right):
            return root_repr(p) == root_repr(q)

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 
        


