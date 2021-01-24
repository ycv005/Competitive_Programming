# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        while l1 and l2:
            t1 = l1.next
            t2 = l2.next

            if l1.val <= l2.val:
                if not head:
                    head = l1
                if t1 and t1.val <= l2.val:
                    l1 = t1
                else:
                    l1.next = l2
                    l1 = t1
            else:
                if not head:
                    head = l2
                if t2 and t2.val < l1.val:
                    l2 = t2
                else:
                    l2.next = l1
                    l2 = t2
        return head

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # print(lists)
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        root = lists[0]
        for i in range(1, len(lists)):
            root = self.mergeTwoLists(root, lists[i])

        return root
