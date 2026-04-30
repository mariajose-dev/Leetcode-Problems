class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n = n & (n - 1)   # removes one '1' bit from the binary version then when 0 stop counting
            count += 1
        return count
        