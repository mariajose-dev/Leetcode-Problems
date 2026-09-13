class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            if s[i]=='b':
                if 'a' in s[i:]:
                    return False
        return True
