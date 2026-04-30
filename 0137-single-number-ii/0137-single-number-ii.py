class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for item in nums:
            if item in dic:
                dic[item]+=1
            else:
                dic[item]=1
        for item in dic:
            if dic[item]==1:
                return item



            
