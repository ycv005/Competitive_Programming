# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315/


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root and arr:
            if not root.left and not root.right and root.val == arr[0] and len(arr)==1:
                return True
            elif root.val == arr[0] and len(arr)!=1:
                return self.isValidSequence(root.left, arr[1:]) or self.isValidSequence(root.right, arr[1:])
        elif not root and not arr:
            return True
        return False
