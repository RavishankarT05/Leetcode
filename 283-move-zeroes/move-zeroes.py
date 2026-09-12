class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i==0:
                nums.append(i)
                nums.remove(i)
        return nums
        # a,b=0,len(nums)-1
        # while a<b:
        #     if nums[a]!=0:
        #         a+=1
        #     if nums[b]==0:
        #         b-=1
        #     if nums[a]==0 and nums[b]!=0:
        #         nums[a],nums[b]=nums[b],nums[a]
        #         a+=1
        #         b-=1
        # return nums