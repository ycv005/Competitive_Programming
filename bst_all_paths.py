# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def printStack(l,stack):
    s = "->".join(map(str,stack))
    l.append(s)

def inOrder(root,l,stack):
    if root:
        stack.append(root.val)
        inOrder(root.left,l,stack)
        if root.left==None and root.right==None:
            printStack(l,stack)
        inOrder(root.right,l,stack)
        stack.pop()

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        l=[]
        stack = []
        inOrder(root,l,stack)
        return l