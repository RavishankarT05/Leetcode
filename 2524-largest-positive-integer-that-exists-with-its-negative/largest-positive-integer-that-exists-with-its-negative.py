class Solution(object):
    def findMaxK(self, nums):
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>0:
                b=-1*(nums[i])
                if b in nums:
                    return nums[i]
            else:
                break
        return -1