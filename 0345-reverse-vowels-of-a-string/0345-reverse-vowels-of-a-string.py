class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        s = list(s)  # strings are immutable → convert to list
    
        vowels = set("aeiouAEIOU")
    
        left = 0
        right = len(s) - 1

        while left < right:
            # move left until vowel
            while left < right and s[left] not in vowels:
                left += 1
        
            # move right until vowel
            while left < right and s[right] not in vowels:
                right -= 1
        
            # swap vowels
            s[left], s[right] = s[right], s[left]
        
            left += 1
            right -= 1

        return "".join(s)
        