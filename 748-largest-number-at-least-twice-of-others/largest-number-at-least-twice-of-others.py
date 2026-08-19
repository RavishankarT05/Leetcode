class Solution(object):
    def dominantIndex(self, nums):
        num=sorted(nums)
        if num[-1]>=(num[-2]*2):
            return nums.index(num[-1])
        return -1