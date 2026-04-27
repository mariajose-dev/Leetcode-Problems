# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head                 # start of odd list
        even = head.next           # start of even list
        even_head = even           # save even head

        while even and even.next:
            odd.next = even.next   # link next odd
            odd = odd.next         # move odd

            even.next = odd.next   # link next even
            even = even.next       # move even

        odd.next = even_head       # attach even list at end

        return head