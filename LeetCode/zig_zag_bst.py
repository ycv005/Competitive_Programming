# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
from collections import deque

# iterative solution using bfs + queue

# data struct of deq is [node, either_left_right, len_zig_zag]

def bfs(root):
    if not root:
        return 0
    deq=deque()
    max_zig_l = 0
    if root.left:
        deq.append([root.left,'l',1])
    if root.right:
        deq.append([root.right, 'r',1])
# now going deeper to the tree as well as checking out the pattern of zig_zag & then increase its val
    while deq:
        node, from_which_side, zig_zag_l = deq.popleft()
        max_zig_l = max(max_zig_l,zig_zag_l)
#         now, going to left of the node

# for increment in the zig_zag_size, we increase using zig_zag_l not max_zig_l
# bcoz max_zig_l takes max till now, we are not sure whether this max will be suitable to zig_zag,
# and since zig_zag_l is increase according to previous stage.
        if node.left:
            if from_which_side=='l': #ok, it came from left side, so no zig_zag formed here
                deq.append([node.left, 'l',1])
            if from_which_side=='r':#ok, it came from right side, so forming a zig_zag pattern here
                deq.append([node.left,'l',zig_zag_l+1])
#        now, going to right of the node
        if node.right:
            if from_which_side=='r': #ok, it came from right side, so no zig_zag formed here
                deq.append([node.right, 'r',1])
            if from_which_side=='l':#ok, it came from left side, so forming a zig_zag pattern here
                deq.append([node.right,'r',zig_zag_l+1])
    return max_zig_l
        
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return bfs(root)