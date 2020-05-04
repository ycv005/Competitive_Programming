class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # LL with 0, 1, 2 length test case, simply return
        if not head or not head.next or not head.next.next: return head
        # head keep track of even pos nodes
        evenHead = ListNode()
        odd = head
        even = head.next
        evenHead.next = even
        # using even & even.next at the end bcoz at the end of each loop,
        # even node is set at last.
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = evenHead.next
        return head
