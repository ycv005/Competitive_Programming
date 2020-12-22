class Solution:
    def __init__(self):
        self.isVaild = True

    def checkBalance(self, root):
        if root and self.isVaild:
            lt = 1 + self.checkBalance(root.left)
            rt = 1 + self.checkBalance(root.right)
            if self.isVaild:
                self.isVaild = abs(lt - rt) <= 1
            return max(lt, rt)
        return 0

    def isBalanced(self, root: TreeNode) -> bool:
        self.checkBalance(root)
        return self.isVaild
