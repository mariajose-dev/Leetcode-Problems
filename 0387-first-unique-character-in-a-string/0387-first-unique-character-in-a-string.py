class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}

        # Step 1: count each character stored in dictionary
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: find first character with count 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
            