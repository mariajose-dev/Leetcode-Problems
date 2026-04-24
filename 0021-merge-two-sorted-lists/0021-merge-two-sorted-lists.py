# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        '''
        l1=[]
        l2=[]
        lis=[]

        while list1:
            l1.append(list1.val)
            list1=list1.next

        while list2:
            l2.append(list2.val)
            list2=list2.next         

        m=len(l1)
        n=len(l2)
        i=0
        j=0
        while i < m and j < n:
            if l1[i] > l2[j]:
                lis.append(l2[j])
                j += 1
            else:
                lis.append(l1[i])
                i += 1

        while i < m:
            lis.append(l1[i])
            i += 1

        while j < n:
            lis.append(l2[j])
            j += 1

        # convert list → linked list
        dummy = ListNode(0)
        current = dummy

        for val in lis:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
        '''

        dummy = ListNode(0)   # temporary node
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next