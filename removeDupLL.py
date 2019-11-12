# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        else:
            t= head
            while t.next!=None:
                if t.val == t.next.val:
                    p = t.next
                    t.next = p.next
                    p = None # it is deleting that node
                else:
                    t = t.next
            return head
