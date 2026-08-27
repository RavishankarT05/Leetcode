class Solution(object):
    def findLengthOfLCIS(self, nums):
        z=[]
        count=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                z.append(count)
                count=1
        z.append(count)
        return max(z)
        