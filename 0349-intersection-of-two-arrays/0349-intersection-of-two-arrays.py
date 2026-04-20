class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        #method1
        return list(set(nums1) & set(nums2)) '''  

        '''
        #method2
        s1=set(nums1)
        s2=set(nums2)

        ans=list(s1.intersection(s2))
        return ans
        '''

        #method3
        set2 = set(nums2)
        result = set()
        
        for num in nums1:
            if num in set2:
                result.add(num)
        
        return list(result)