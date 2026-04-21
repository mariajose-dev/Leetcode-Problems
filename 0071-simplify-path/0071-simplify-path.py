class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        input = path.split('/')   # split by '/'
        stack = []

        for x in input:           # use input, not path
            if x == '' or x == '.':
                continue
            elif x == '..':
                if stack:        # avoid popping empty stack
                    stack.pop()
            else:
                stack.append(x)

        return '/' + '/'.join(stack)