class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_set = set()

        for ch in s:
            if ch in my_set:
                return ch
            my_set.add(ch)
                
        