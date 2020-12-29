# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter


class Solution:
    def __init__(self):
        self.count = 0

    def doTraversal(self, root, freq):
        if root:
            # exploring node
            if root.val in freq:
                freq[root.val] += 1
            else:
                freq[root.val] = 1
            self.doTraversal(root.left, freq)
            self.doTraversal(root.right, freq)
            if not root.left and not root.right:
                # this is the end, we got a freq of a path
                oddCount = 0
                for k, v in freq.items():
                    if v % 2 != 0:
                        oddCount += 1
                    if oddCount > 1:
                        break
                if oddCount <= 1:
                    self.count += 1

            # done with exploration
            freq[root.val] -= 1
            if freq[root.val] == 0:
                del freq[root.val]

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 0
        freq = {}
        self.doTraversal(root, freq)
        return self.count
