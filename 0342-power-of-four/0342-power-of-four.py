class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0,31):
            if 4**i==n:
                return True
            
        return False