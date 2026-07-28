class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                a.append(count)
                count=0
        a.append(count)
        a.sort()
        return a[-1]
