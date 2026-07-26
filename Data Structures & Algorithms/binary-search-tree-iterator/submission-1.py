# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.stack = []
        

    def next(self) -> int:
        while self.curr or len(self.stack)>0:
            if self.curr:
                self.stack.append(self.curr)
                # print(f'added to stack {self.curr.val}')
                self.curr = self.curr.left
            else:
                # print(f"[NEXT befor pop] curr: {self.curr} stack: {self.stack}")
                item = self.stack.pop()
                if item.right:
                    # self.stack.append(item.right)
                    self.curr = item.right
                # print(f"[NEXT] {item.val} curr: {self.curr} stack: {self.stack} {self.stack[0].val if len(self.stack) >= 1 else ''} {self.stack[1].val  if len(self.stack) >= 2 else ''}")
                return item.val

        

    def hasNext(self) -> bool:
        # print(f"[HAS_NEXT] curr: {self.curr} stack: {self.stack}")
        if self.curr or len(self.stack)>0:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()