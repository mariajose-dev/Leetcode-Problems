class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        ls=tickets[k]
        time=0
        for i in range(len(tickets)):
            if i>k and tickets[i]>=ls:
                time=time+(ls-1)
            elif tickets[i]<ls:
                time=time+tickets[i]
            else:
                time+=ls
        return time

