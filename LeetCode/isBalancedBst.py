def isBalancedBst(root,wrapper):
    if root==None:
        return 0
    elif wrapper[0]!=False:
        l=r=0
        if root.left!=None:
            l= 1 + (isBalancedBst(root.left,wrapper) or 0)
        if root.right!=None:
            r= 1 + (isBalancedBst(root.right,wrapper) or 0)
        if abs(l-r)>1:
            wrapper[0]=False
        return max(l,r)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        wrapper=[True]
        isBalancedBst(root,wrapper)
        return wrapper[0]
        # https://leetcode.com/problems/balanced-binary-tree/