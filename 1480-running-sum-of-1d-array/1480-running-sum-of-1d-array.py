class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        sum_nums=sum(nums)
        for i in range(len(nums)-1,-1,-1):
            ans.append(sum_nums)
            sum_nums-=nums[i]
        return ans[::-1]