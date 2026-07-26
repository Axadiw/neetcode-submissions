# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if q.val < p.val:
            tmp = q
            q = p
            p = tmp

        # print(f"p: {p.val} q: {q.val}")
        def LCA(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            print(f"root is {root.val}")
            if root.val == p.val or root.val == q.val or (p.val < root.val and root.val < q.val):
                return root
            
            if p.val < root.val and q.val < root.val:
                return LCA(root.left, p, q)
            if p.val > root.val and q.val > root.val:
                return LCA(root.right, p, q)
            
            return None
        
        return LCA(root, p,q)