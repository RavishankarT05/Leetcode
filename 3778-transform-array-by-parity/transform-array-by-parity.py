class Solution(object):
    def transformArray(self, nums):
        return sorted([0 if x%2==0 else 1 for x in nums])
        