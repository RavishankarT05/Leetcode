class Solution(object):
    def minimumCost(self, nums):
        a=sorted(nums)
        # print(nums)
        # count=0
        # a=0
        # while a<len(nums)-1:
        #     if nums[a]==nums[a+1]:
        #         count+=nums[a]+nums[a+1]
        #         a+=2
        #     count+=nums[a]
        #     a+=1
        # return count
        a.remove(nums[0])
        return nums[0]+a[0]+a[1]