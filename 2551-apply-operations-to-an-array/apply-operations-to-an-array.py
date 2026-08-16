class Solution(object):
    def applyOperations(self, nums):
        a,b=0,1
        while a<len(nums) and b<len(nums):
            if nums[a]==nums[b]:
                nums[a]+=nums[b]
                nums[b]=0
                a+=2
                b+=2
            else:
                a+=1
                b+=1
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        return nums