# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
                return None
            
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])

        root = preorder[0]
        index_of_root_in_inorder = inorder.index(root)
        l_inorder = inorder[:index_of_root_in_inorder]
        r_inorder = inorder[index_of_root_in_inorder+1:]

        l_preorder = preorder[1:1+len(l_inorder)]
        r_preorder = preorder[1+len(l_inorder):]

        return TreeNode(val=root, left=self.buildTree(l_preorder,l_inorder), right=self.buildTree(r_preorder,r_inorder)) 
        