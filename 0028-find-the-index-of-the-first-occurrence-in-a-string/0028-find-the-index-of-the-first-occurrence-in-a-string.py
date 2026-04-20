class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        '''
        #method 1
        return haystack.find(needle)
        '''

        #method 2
        n = len(needle)
        m = len(haystack)

        if n == 0:
            return 0

        for i in range(m - n + 1):
            # check first and last character (your idea)
            if haystack[i] == needle[0] and haystack[i + n - 1] == needle[-1]:
                
                # check full substring
                if haystack[i:i+n] == needle:
                    return i
        
        return -1
