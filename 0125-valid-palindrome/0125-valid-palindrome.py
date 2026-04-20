class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #here each char in s make lowercase iff its alpha numeric then add to 'cleaned'
        #then compare the cleaned and reverse of cleaned
        
        cleaned = "".join(char for char in s.lower() if char.isalnum())
    
        return cleaned == cleaned[::-1]