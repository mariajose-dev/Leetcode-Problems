class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        dic={}
        for x in bulbs:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        lis=[]
        for x in dic:
            if dic[x]%2!=0:
                lis.append(x)
        lis.sort()
        return lis