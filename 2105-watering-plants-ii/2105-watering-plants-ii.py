class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        left = 0
        right = len(plants) - 1
        
        waterA = capacityA
        waterB = capacityB
        
        refills = 0
        
        while left < right:
            # Alice
            #refill condition
            if waterA < plants[left]:
                refills += 1
                waterA = capacityA
            waterA -= plants[left] #real watering done ; water left
            left += 1 # move to next plant

            # Bob
            #refill condition
            if waterB < plants[right]:
                refills += 1
                waterB = capacityB
            waterB -= plants[right] #real watering done ; water left
            right -= 1 # move to next plant
        
        # If both meet at same plant
        if left == right:
            if max(waterA, waterB) < plants[left]:
                refills += 1
        
        return refills
        