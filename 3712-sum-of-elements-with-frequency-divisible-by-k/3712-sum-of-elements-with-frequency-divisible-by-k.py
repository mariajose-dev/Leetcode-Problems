class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic={}
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1

        sum=0
        for x in dic:
            if dic[x]%k==0:
                sum+=x*dic[x]
        return sum