class Solution(object):
    def maxProduct(self, nums):
        a=list(sorted(nums))
        return (a[-1]-1)*(a[-2]-1)
        