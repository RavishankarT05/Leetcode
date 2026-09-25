class Solution(object):
    def sortArrayByParity(self, nums):
        a,b=0,len(nums)-1
        while a<b:
            if nums[b]%2==0 and nums[a]%2!=0:
                nums[a],nums[b]=nums[b],nums[a]
            if nums[a]%2==0:
                a+=1
            if nums[b]%2!=0:
                b-=1
        return nums
