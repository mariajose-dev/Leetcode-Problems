class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j=0
        #copy value of nonzero position to first of loop
        for i in range (len(nums)):
            if(nums[i]!=0):
                nums[j]=nums[i]
                j=j+1
        #last add zeros 
        while(j<len(nums)):
            nums[j]=0
            j=j+1

        
        


            
        
        


        