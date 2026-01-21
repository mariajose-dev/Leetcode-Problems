class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        orginal=x
        while(x!=0):
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if(orginal==rev):
            return True
        else:
            return False

        