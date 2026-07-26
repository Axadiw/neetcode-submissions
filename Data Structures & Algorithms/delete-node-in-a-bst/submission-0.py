# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def searchNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    #     if not root:
    #         return None

    #     if root.val > key:
    #         return root.right
    #     elif root.val < key:
    #         return root.left
    #     else:
    #         return root
    
    def findMinimalNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root

        while current and current.left:
            current = current.left
        
        return current        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            print(f"not root")
            return root
        print(f'suwam key {key}, root: {root.val} left: {root.left} right: {root.right}')
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            print(f"usuwam {key}")
            if not root.left and not root.right:
                return None

            if root.left and root.right:
                minimal_node = self.findMinimalNode(root.right)                                
                root.val = minimal_node.val
                root.right = self.deleteNode(root.right, minimal_node.val)

            elif root.left:
                return root.left
            
            elif root.right:
                return root.right
        return root


            
            

        

