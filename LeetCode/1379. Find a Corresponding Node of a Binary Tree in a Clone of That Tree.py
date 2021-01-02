# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path = None
        self.ref = None

    def doInorderTrav(self, root, path, ref):
        if root and self.path == None:
            self.doInorderTrav(root.left, path + "l", ref)
            if ref == root:
                self.path = path
                return
            self.doInorderTrav(root.right, path + "r", ref)

    def getReference(self, root, path, i):
        if root and self.ref == None:
            if i == len(path):
                self.ref = root
            elif i < len(path):
                way = path[i]
                if way == "l":
                    self.getReference(root.left, path, i+1)
                else:
                    self.getReference(root.right, path, i + 1)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.doInorderTrav(original, "", target)
        self.getReference(cloned, self.path, 0)
        return self.ref
