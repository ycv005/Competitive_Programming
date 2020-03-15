# https://leetcode.com/problems/binary-tree-inorder-traversal/
def inorderTrav(root, a):
    if root:
        inorderTrav(root.left,a)
        a.append(root.val)
        inorderTrav(root.right,a)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a=[]
        inorderTrav(root,a)
        return a