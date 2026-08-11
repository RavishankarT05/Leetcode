class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            b=sum(map(int, str(nums[i])))
            if i==b:
                return b
        return -1