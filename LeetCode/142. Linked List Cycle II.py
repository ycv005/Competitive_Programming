class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        slow = head
        fast = head
        thirdPt = None
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                thirdPt = head
                break
        if slow!=fast:
            return None
        while thirdPt and slow and thirdPt!=slow:
            thirdPt=thirdPt.next
            slow=slow.next
        return thirdPt if thirdPt==slow else None
