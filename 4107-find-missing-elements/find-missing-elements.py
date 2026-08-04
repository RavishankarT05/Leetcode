class Solution(object):
    def findMissingElements(self, nums):
        a=[]
        for i in range(min(nums),max(nums)):
            if i not in nums:
                a.append(i)
        return a
