# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l=ListNode(0)
        r=l
        t=l1
        p=l2
        if p==None or t==None:
            return t or p
        elif p==None and t==None:
            return l1
        while t!=None:
            while p!=None:
                if t!=None and t.val<=p.val:
                    r.next=ListNode(t.val)
                    t=t.next
                else:
                    r.next=ListNode(p.val)
                    p=p.next
                r=r.next
            if p==None and t!=None:
                # print("full append p")
                r.next=t
                break
        l=l.next
        return l