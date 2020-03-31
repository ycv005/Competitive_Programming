def getMidElement(node):
    if node:
        slow=fast=node
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    return None

def reverseLL(node):
    if node:
        prev=None
        curr=node
        nxt = curr.next
        while curr and curr.next:
            curr.next=prev
            prev=curr
            curr = nxt
            nxt=nxt.next
        curr.next=prev
        return curr

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        t1=head
        t2=getMidElement(head)
        if t1==t2: #single element or None
            return True
        t2=reverseLL(t2)
        while t1 and t2:
            if t1.val!=t2.val:
                return False
            t1=t1.next
            t2=t2.next
        return True
