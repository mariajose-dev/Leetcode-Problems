class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        step=0
        can=capacity #initially can has full capacity
        for i in range (len(plants)):
            if (plants[i]<=can):
                can=can-plants[i]
                step=step+1
            else:
                step=step+2*i+1
                can=capacity-plants[i]
                # or can=capacity then can=can-plant[i] direct step above
        return step

        