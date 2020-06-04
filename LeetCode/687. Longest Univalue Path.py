class Solution:
    def __init__(self):
        self.ans = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.getLongestPath(root)
        return self.ans

    def getLongestPath(self, root):
        if not root: return 0
        left_same_length = self.getLongestPath(root.left)
        right_same_lenght = self.getLongestPath(root.right)

        curr_left_length = curr_right_length = 0
        if root.left and root.left.val == root.val:
            curr_left_length = 1 + left_same_length
        if root.right and root.right.val == root.val:
            curr_right_length = 1 + right_same_lenght
        self.ans = max(self.ans, curr_left_length + curr_right_length)

        return max(curr_left_length, curr_right_length)
