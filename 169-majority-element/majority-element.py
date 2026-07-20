class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)//2
        nums.sort()
        print(nums)
        return nums[n]
        