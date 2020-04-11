def getDiameter(root,h,mx):
    if root:
        left = 1 + getDiameter(root.left,h+1,mx) if root.left else 0
        right = 1 + getDiameter(root.right,h+1,mx) if root.right else 0
        mx[0] = mx[0] if mx[0]>abs(right+left) else abs(right+left)
        return max(right,left)
    return 0

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        mx= [0]
        getDiameter(root,0,mx)
        return mx[0]
