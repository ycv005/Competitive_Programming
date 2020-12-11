# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def goLeft(self, root):
        if root:
            self.stack.append(root)
            self.goLeft(root.left)

    def doProcess(self, root):
        if root and root.right:
            self.stack.append(root.right)
            self.goLeft(root.right.left)

    def __init__(self, root: TreeNode):
        self.stack = []
        self.goLeft(root)

    def next(self) -> int:
        tmp = self.stack.pop()
        self.doProcess(tmp)
        return tmp.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

        # Your BSTIterator object will be instantiated and called as such:
        # obj = BSTIterator(root)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()
