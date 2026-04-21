class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for x in s:
            if stack and x=='B' and stack[-1]=='A':
                stack.pop()
            elif stack and x=='D' and stack[-1]=='C':
                stack.pop()
            else:
                stack.append(x)

        return len(stack)        