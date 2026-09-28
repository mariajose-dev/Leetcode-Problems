class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis=s.split()
        ans=""
        for x in lis:
            ans+=x[::-1]+" "
        return ans[:-1]