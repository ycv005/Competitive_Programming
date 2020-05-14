class Solution:
    def inOrder(self, root, wrapper):
        if root:
            self.inOrder(root.left, wrapper)
            wrapper[1].append(root.val)
            if len(wrapper[1]) == 2:
                tmp = wrapper[1][1] - wrapper[1][0]
                if tmp<wrapper[0]:
                    wrapper[0] = tmp
                # pop first element, as next time we need to test last & upcoming val
                wrapper[1] = [wrapper[1][1]]
            self.inOrder(root.right, wrapper)

    """In inorder traversal, diff b/w two consecutive element gives min. val"""
    def minDiffInBST(self, root: TreeNode) -> int:
        # wrapper = [minVal, two consecutive val]
        wrapper = [float('inf'),[]]
        self.inOrder(root, wrapper)
        return wrapper[0]
