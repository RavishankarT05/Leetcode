class Solution(object):
    def countPairs(self, nums, target):
    #     if range
    #     i,j=0,1
    #     while





        count=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    count+=1
        return count
