# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lis1=[]
        lis2=[]

        while l1:
            lis1.append(l1.val)
            l1=l1.next

        #print(lis1)
        num1=int("".join(map(str, lis1)))
        print(num1)

        while l2:
            lis2.append(l2.val)
            l2=l2.next

        #print(lis2)
        num2=int("".join(map(str, lis2)))
        print(num2)

        num3=num1+num2
        print(num3)

        lis3=list(map(int, str(num3)))
        print(lis3)

        dummy=ListNode(0)
        temp=dummy

        for item in lis3:
            temp.next=ListNode(item)
            temp=temp.next
        return dummy.next