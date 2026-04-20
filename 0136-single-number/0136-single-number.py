class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        #method 1
        for item in nums:
            if nums.count(item)==1:
                return item
        '''
        #method 2
        result = 0
        for n in nums:
            result ^= n
        return result