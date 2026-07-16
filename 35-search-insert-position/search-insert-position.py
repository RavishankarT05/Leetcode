class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            a=nums.index(target)
            return a
        else:
            for i in nums:
                if target<i:
                    b=nums.index(i)
                    return b
        b=len(nums)
        return b