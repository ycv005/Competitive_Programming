def ll_length(head):
    l=0
    while head:
        l+=1
        head = head.next
    return l

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         using length to cut down the unnecessary rotation
        if head==None:
            return head
        ll = ll_length(head)
        k= k%(ll)
        if k!=0:
            head1=head
            for i in range(ll-k-1):
                head1=head1.next
            t=head1.next
            head1.next = None
            # t is head actually
            tmp = t
            while tmp.next:
                tmp = tmp.next
            tmp.next= head
            return t
        return head
