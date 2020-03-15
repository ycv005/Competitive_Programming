# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next==None:
            return head
        dum = ListNode(0)
        prev = ListNode(0)
        cur = head
        nxt = head.next
        i=0
        while nxt!=None:
            i+=1
            t = nxt.next
            nxt.next = cur
            cur.next = t
            prev.next = nxt
            if i==1:
                dum.next = nxt
            if t==None or t.next==None:
                break
            prev = cur
            cur = t
            nxt = t.next
        return dum.next
