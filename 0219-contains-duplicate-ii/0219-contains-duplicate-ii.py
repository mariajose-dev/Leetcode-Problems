class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        ws=set()
        #k is window size
        for i in range(n):
            if i>k:
                ws.remove(nums[i-k-1])
            if(nums[i] in ws):
                return True
            ws.add(nums[i])
        return False

        
        