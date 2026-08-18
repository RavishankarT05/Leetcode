class Solution(object):
    def differenceOfSum(self, nums):
        a=sum(nums)
        b=0
        for i in nums:
            b+=sum(map(int,str(i)))
        return abs(a-b)