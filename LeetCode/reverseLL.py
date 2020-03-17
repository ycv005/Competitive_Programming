class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev= None
        if not curr or not curr.next: # None or only 1 LL
            return head
        nxt = curr.next
        while curr.next:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        curr.next = prev
        return curr
        # https://leetcode.com/problems/reverse-linked-list/