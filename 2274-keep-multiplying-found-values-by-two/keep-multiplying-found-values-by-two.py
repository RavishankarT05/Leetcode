class Solution(object):
    def findFinalValue(self, nums, original):
        if original not in nums:
            return original
        while True:
            if original*2 not in nums:
                return original*2
            else:
                original*=2
            
