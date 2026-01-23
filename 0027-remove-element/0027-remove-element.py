class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=0
        #copy value of nonzero position to first of loop
        for i in range (len(nums)):
            if(nums[i]!=val):
                nums[j]=nums[i]
                j=j+1
        return j
        