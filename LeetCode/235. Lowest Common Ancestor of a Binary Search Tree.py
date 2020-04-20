def searchNode(root,p,q):
    if root:
        if p.val<root.val and q.val<root.val:
            return searchNode(root.left,p,q)
        elif p.val>root.val and q.val>root.val:
            return searchNode(root.right,p,q)
        return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None: return root
        return searchNode(root,p,q)


#------------------Other shorter way------------

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None: return root
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
