def inOrder(root,wrapper):
    if root.left!=None:
        r = inOrder(root.left,wrapper)
        if r==False:
            return False
    if wrapper[0]!=None and wrapper[0].val>=root.val:
        return False
    wrapper[0] = root
    if root.right!=None:
        r= inOrder(root.right,wrapper)
        if r==False:
            return False
    
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        res= None
        wrapper = [res]
        t=inOrder(root,wrapper)
        if(None==t):
            t=True
        return t
# I have used wrapper because- https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference