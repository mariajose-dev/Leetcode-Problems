class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []      # to store numbers
        num = 0         # current number
        sign = '+'      # previous operator

        for i in range(len(s)):

            # build number (handles multi-digit like 12, 123)
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            # if operator OR last character → process previous number
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)         # push positive number

                elif sign == '-':
                    stack.append(-num)        # push negative number

                elif sign == '*':
                    stack.append(stack.pop() * num)   # multiply immediately

                elif sign == '/':
                    a = stack.pop()
                    stack.append(int(float(a) / num))  

                sign = s[i]   # update operator * CUT + changes 
                num = 0       # reset number

        return sum(stack)     # final result sum of stack
