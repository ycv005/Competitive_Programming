# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return False
        else:
            l=head
            r=head.next
            flag =0
            while r!=None and l!=None:
                if l==r:
                    flag = 1
                    break
                if l.next==None or r.next==None:
                    flag =0
                    break
                l=l.next
                r=r.next.next
            return True if flag==1 else False
