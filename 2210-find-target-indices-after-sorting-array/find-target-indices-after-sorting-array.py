class Solution(object):
    def targetIndices(self, nums, target):
        nums=list(sorted(nums))
        a=[]
        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)
        return a