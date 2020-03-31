def getLength(node):
    t=node
    i=0
    while t:
        t=t.next
        i+=1
    return i

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        la=getLength(headA)
        lb=getLength(headB)
        t=abs(la-lb)
        t1=headA
        t2=headB
        if la>lb: #mean list A has to go ahead by t
            while t:
                t1=t1.next
                t-=1
        else: # list B has to go ahead by t
            while t:
                t2=t2.next
                t-=1
        while t1 and t2:
            if t1==t2:
                return t1
            t1=t1.next
            t2=t2.next
        return None
