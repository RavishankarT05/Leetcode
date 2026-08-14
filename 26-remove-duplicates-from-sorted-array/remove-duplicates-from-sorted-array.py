class Solution(object):
    def removeDuplicates(self, nums):
        # for i in nums:
        #     a=nums.count(i)
        #     while a>1:
        #         nums.remove(i)
        #         a-=1

        a,b=0,1
        while b<len(nums):
            if nums[a]==nums[b]:
                b+=1
            else:
                a+=1
                nums[a],nums[b]=nums[b],nums[a]
                b+=1
        return a+1