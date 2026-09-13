class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'a' not in s:
            return True

        stk=[]
        for i in range(len(s)):
            if s[i]=='a':
                stk.append(s[i])
            else:
                if 'a' in s[i:]:
                    return False
        return True
