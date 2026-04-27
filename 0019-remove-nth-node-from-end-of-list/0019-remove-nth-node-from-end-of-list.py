class Solution(object):
    def removeNthFromEnd(self, head, n):

        lis1 = []
        temp = head   # preserve original head

        while temp:
            lis1.append(temp.val)
            temp = temp.next

        m = len(lis1) - n

        # delete first node
        if m == 0:
            return head.next

        co = 0
        temp = head

        # go to (m-1)th node
        while co < m - 1:
            temp = temp.next
            co += 1

        # delete node
        temp.next = temp.next.next

        return head
       
        