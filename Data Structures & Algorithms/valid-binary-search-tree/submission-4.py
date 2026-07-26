# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class AncestorItem:
    def __init__(self, val:int, greater: bool):
        self.val = val
        self.greater = greater
    
    # @property
    # def val(self):
    #     return self.val
    
    # @property
    # def greater(self):
    #     return self.greater
    
    def test(self, value: int):        
        if self.greater:
            print(f" {value} > {self.val} is greater {value > self.val}")
            return value > self.val
        else:
            print(f" {value} < {self.val} is lower {value < self.val}")
            return value < self.val
    
    def __repr__(self):
        return f"{self.val} greater: {self.greater}"


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        def isValidBSTWithAncestors(root: Optional[TreeNode], ancestors: List[AncestorItem]) -> bool:        
            if not root:
                return True

            
            left_satisfied = root.left.val < root.val if root.left else True
            right_satisfied = root.right.val > root.val if root.right else True
            ancestors_array = [x.val for x in ancestors if not x.test(root.val)]
            ancestors_satisfied = len(ancestors_array) == 0
            # print(f"{root.val} LEFT: {root.left.val if root.left else 'none'} RIGHT: {root.right.val if root.right else 'none'} ancestors_satisfied: {ancestors_satisfied} ancestors_array: {ancestors_array} ancestors: {[x for x in ancestors]}")

            left_decendants_satisfied = isValidBSTWithAncestors(root.left, ancestors + [AncestorItem(val=root.val, greater=False)])
            right_decendants_satisfied = isValidBSTWithAncestors(root.right, ancestors + [AncestorItem(val=root.val, greater=True)])
            return left_satisfied and right_satisfied and left_decendants_satisfied and right_decendants_satisfied and ancestors_satisfied
        
        return isValidBSTWithAncestors(root, [])