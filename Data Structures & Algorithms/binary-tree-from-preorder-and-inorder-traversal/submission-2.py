# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # def get_index_of_element(list: List[int], element: int) -> int:
        #     for index, item in enumerate(list):
        #         if item == element:
        #             return index
        #     return -1

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
        l_root = self.buildTree(l_preorder,l_inorder)
        r_root = self.buildTree(r_preorder,r_inorder)

        # print('=======')
        # print(f"preorder: {preorder}")
        # print(f"inorder: {inorder}")
        # print(f"index_of_root_in_inorder: {index_of_root_in_inorder}")
        # print(f"root: {root}")

        # print(f"l_preorder: {l_preorder}")
        # print(f"l_inorder: {l_inorder}")
        # print(f"r_preorder: {r_preorder}")
        # print(f"r_inorder: {r_inorder}")

        # print(f"l_root: {l_root}")
        # print(f"r_root: {r_root}")
        # print('=======')

        return TreeNode(val=root, left=l_root, right=r_root) 
        