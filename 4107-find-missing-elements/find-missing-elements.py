class Solution(object):
    def findMissingElements(self, nums):
        a=[]
        nums=set(nums)
        for i in range(min(nums)+1,max(nums)):
            if i not in nums:
                a.append(i)
        return a
