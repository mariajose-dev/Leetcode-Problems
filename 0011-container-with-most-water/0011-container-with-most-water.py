class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0                      # left pointer (start of array)
        j = len(height) - 1        # right pointer (end of array)
        max_area = 0              # store maximum area found

        while i < j:              # continue until pointers meet
            # width between two lines
            width = j - i         
            
            # height is limited by the shorter line
            h = min(height[i], height[j])
            
            # calculate current area
            area = width * h      
            
            # update maximum area if current is larger
            max_area = max(max_area, area)

            # move the pointer pointing to the smaller height
            # because only that can potentially increase area
            if height[i] < height[j]:
                i += 1            # move left pointer right
            else:
                j -= 1            # move right pointer left

        return max_area           # return the best area found

        