class Solution(object):
    def sortArrayByParityII(self, nums):
        a,b=0,1
        while a<len(nums) and b<len(nums):
            if nums[a]%2!=0:
                if nums[b]%2==0:
                    nums[a],nums[b]=nums[b],nums[a]
                else:
                    b+=2
            else:
                a+=2
        return nums

            