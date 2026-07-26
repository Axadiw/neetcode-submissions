# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        items = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                items.append('')
                return
            
            items.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(f"serizalize {items}")
        return ','.join(items)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:        
        items = deque(data.split(','))
        print(f"deserizalize {items}")
        
        if len(items) == 0:
            return None
        
        def dfs() -> Optional[TreeNode]:
            rootVal = items.popleft()
            if not rootVal:
                return None

            root = TreeNode(val=rootVal)
            root.left = dfs()
            root.right = dfs()
            
            return root

            
        
        return dfs()
