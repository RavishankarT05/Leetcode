class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        a=0
        count=0
        for _ in range(len(nums)/2):
            count+=nums[a]
            a+=2
        return count
        nums.sort()
        return sum(nums[::2])