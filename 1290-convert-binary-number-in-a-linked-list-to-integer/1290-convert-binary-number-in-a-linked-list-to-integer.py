# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        lis1=[]
        while head:
            lis1.append(head.val)
            head=head.next
        print(lis1)

        sum=0
        n=len(lis1)
        i=0
        j=n-1

        for i in range(n):
            sum+=lis1[i]*(2**j)
            j=j-1
            i=i+1

        return sum

        