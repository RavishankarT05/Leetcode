class Solution(object):
    def check(self, nums):
        num=sorted(nums)
        c=len(nums)
        while c>0:
            if num==nums:
                return True
            else:
                nums[:]=nums[1:]+nums[:1]
            c-=1
        return False
        