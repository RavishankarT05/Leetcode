class Solution(object):
    def countPairs(self, nums, target):
        # i,j=0,1
        # count=0
        # while i<len(nums)-1:
        #     if nums[i] + nums[j] < target:
        #         count+=1
        #         j+=1
        #     else:
        #         j+=1
        #     if j==len(nums):
        #         i+=1
        #         j=i+1 
        # return count
        count=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    count+=1
        return count
