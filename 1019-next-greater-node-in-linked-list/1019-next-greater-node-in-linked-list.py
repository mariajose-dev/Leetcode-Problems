# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        res = [0] * len(vals)
        st = []   # stack of indices

        for i in range(len(vals)):
            while st and vals[i] > vals[st[-1]]:
                idx = st.pop()
                res[idx] = vals[i]
            st.append(i)

        return res
        