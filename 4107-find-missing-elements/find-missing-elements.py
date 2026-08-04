class Solution(object):
    def findMissingElements(self, nums):
        a=[]
        nums.sort()
        b=nums[0]
        c=nums[-1]
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                a.append(i)
        return a
