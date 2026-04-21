class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ['a']

        for x in s:
            if (x==')' and stack[-1]=='('):  
                stack.pop()
            elif (x=='}' and stack[-1]=='{'): 
                stack.pop()
            elif (x==']' and stack[-1]=='['):  
                stack.pop()
            else:
                stack.append(x)

        if len(stack)==1:
            return True
        else:
            return False