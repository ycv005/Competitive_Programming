class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            a = self.searchBST(root.left, val)
            b = self.searchBST(root.right, val)
            return a if a else b
