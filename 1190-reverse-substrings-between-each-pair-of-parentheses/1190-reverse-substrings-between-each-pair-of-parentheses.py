class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stk=[]

        for x in s:
            if x!='(' and x!=')':
                stk.append(x)

            elif x=='(':
                stk.append(x)

            elif x==')':
                ans=""

                while stk[-1]!='(':
                    a=stk.pop()
                    ans+=a

                stk.pop()

                for y in ans:
                    stk.append(y)

        return "".join(stk)
