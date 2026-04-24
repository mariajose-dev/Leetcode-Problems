# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # first take all the data part of LL elements
        lis=[]
        while head:
            lis.append(head.val)
            head=head.next

        #print(lis)

        #check frequency of each element in list and make dictionary
        dic={}
        for x in lis:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1

        #print(dic)

        #if frequency = 1 add to stack
        stack=[]
        for x in lis:
            if dic[x]==1:
                stack.append(x)

        #print(stack)

        #now add stack elements to list one by one
        dummy=ListNode(0)
        temp=dummy

        for item in stack:
            temp.next=ListNode(item)
            temp=temp.next    
        return dummy.next
