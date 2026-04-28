class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={}
        for item in nums:
            if item in dic:
                dic[item]+=1
            else:
                dic[item]=1
        print(dic)

        for item in dic:
            if dic[item]>=2:
                return True
        return False
