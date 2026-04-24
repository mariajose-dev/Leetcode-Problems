# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lis=[]
        while head:
            lis.append(head.val)
            head=head.next
        print(lis)

        lis.reverse()
        print(lis)

        dummy=ListNode(0)
        temp=dummy

        for item in lis:
            temp.next=ListNode(item)
            temp=temp.next    
        return dummy.next
        