# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # already distinct base case
        if not head or not head.next:
            return head
        prev = None
        curr = head
        nxt = head.next
        dup = False
        beforeNext = curr

        while nxt:
            if curr.val == nxt.val:
                # find dup
                beforeNext = nxt
                nxt = nxt.next
                dup = True
            else:
                # handle prev find dup
                if dup:
                    if not prev:
                        head = nxt
                        curr = head
                        if nxt:
                            nxt = nxt.next
                    else:
                        if prev:
                            prev.next = nxt
                        curr = nxt
                        if nxt:
                            nxt = nxt.next

                    beforeNext = None
                    dup = False
                else:
                    # didn't find any duplicate
                    prev = curr
                    curr = nxt
                    if nxt:
                        nxt = nxt.next

            if dup and not nxt:
                # there is duplicate and reach to the end
                if prev:
                    prev.next = nxt
                else:
                    head = nxt

        return head
