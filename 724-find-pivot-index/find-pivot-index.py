class Solution(object):
    def pivotIndex(self, nums):
        l=0
        t=sum(nums)
        c=0
        for i,num in enumerate(nums):
            if l==t-l-num:
                return i
            l+=num
        return -1