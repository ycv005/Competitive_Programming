class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0 or len(inorder)==0:
            return None
        root = TreeNode()
#         getting head of Tree/subTree
        root.val = preorder.pop(0)
        ind = inorder.index(root.val)
        inOrder_left = inorder[:ind]
        # inOrder_right = inorder[ind+1:] #leaving root
        # preOrder_left = preorder[:len(inOrder_left)]
        # preOrder_right = preorder[len(inOrder_left):]
        root.left = self.buildTree(preorder[:len(inOrder_left)],inOrder_left)
        root.right = self.buildTree(preorder[len(inOrder_left):],inorder[ind+1:])
        return root
        # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/