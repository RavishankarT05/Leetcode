class Solution(object):
    def isGood(self, nums):
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            if nums[i]==i+1:
                pass
            else:
                return False
        if len(nums)<2:
            return False
        return nums[-1]==nums[-2]        
