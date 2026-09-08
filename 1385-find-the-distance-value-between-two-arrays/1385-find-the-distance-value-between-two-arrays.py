class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        co=0

        for x in arr1:
            flag=1

            for y in arr2:
                if abs(x-y)<=d:
                    flag=0
                    break

            if flag==1:
                co+=1

        return co