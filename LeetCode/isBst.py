def inOrder(root, wrapper):
    if root and wrapper[1]!=False:
        inOrder(root.left, wrapper)
        if wrapper[0]!=None and wrapper[0].val>=root.val:
            # print("comparing-as wrapper, root",wrapper[0].val,root.val)
            wrapper[1]=False
        wrapper[0]=root
        inOrder(root.right, wrapper)
    
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        node,isBst = None, True
        wrapper = [node, isBst]
        inOrder(root, wrapper)
        return wrapper[1]