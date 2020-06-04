class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N==1: return [TreeNode()]
        if N%2==0: return []

        res = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N -1 -i):
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
