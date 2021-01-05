# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head, p):
        # return head and tail
        if not head or not head.next:
            if p:
                p.next = head
            return [head, head]
        prev = p
        cur = head
        nxt = head.next
        while cur:
            cur.next = prev
            prev = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        if p:
            p.next = prev
        return [prev, head]

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # base case
        if not head or not head.next or k == 1:
            return head
        else:
            f = head
            prev = None
            returnHead = None
            exitLoop = False
            while f:
                tmp = k - 1
                l = f
                while tmp > 0:
                    if l:
                        l = l.next
                        if not l and k > 0:
                            exitLoop = True
                            break
                    else:
                        exitLoop = True
                        break
                    tmp -= 1
                if exitLoop:
                    break
                if l:
                    ahead = l.next
                else:
                    ahead = None
                # before calling
                if l:
                    l.next = None
                newHead, newTail = self.reverseLL(f, prev)
                if not prev:
                    returnHead = newHead
                prev = newTail
                prev.next = ahead
                f = ahead
            return returnHead
