class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        a=nums[0]
        b=nums[-1]
        c=b
        while 0<c:
            if a%c==0 and b%c==0:
                return c
            c-=1
        return c