# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        temp = dummy
        total = 0

        cur = head.next   # skip first 0

        while cur:
            if cur.val == 0:
                # end of a block → create node
                temp.next = ListNode(total)
                temp = temp.next
                total = 0            # reset sum
            else:
                total += cur.val     # accumulate

            cur = cur.next

        return dummy.next