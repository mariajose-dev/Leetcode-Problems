class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            num=nums[i]
            sum=0
            while num!=0:
                r=num%10
                num=num//10
                sum+=r
            if sum==i:
                return i
        return -1