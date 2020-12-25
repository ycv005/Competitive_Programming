# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # when the ll is 0 or 1 of length
        if not head or not head.next:
            return head
        just_prev = None
        prev = head
        cur = head.next
        tmp = head.next
        while cur and prev:
            prev.next = cur.next
            cur.next = prev
            if just_prev:
                just_prev.next = cur
                just_prev = prev
            elif not just_prev:
                just_prev = prev
            prev = prev.next
            if prev:
                cur = prev.next
        return tmp
