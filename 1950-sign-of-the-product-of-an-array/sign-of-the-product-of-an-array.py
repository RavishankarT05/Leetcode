class Solution(object):
    def arraySign(self, nums):
        count=1
        for i in nums:
            count*=i
        if count==0:
            return 0
        elif count<0:
            return -1
        else:
            return 1 
        