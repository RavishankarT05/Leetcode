class Solution(object):
    def differenceOfSum(self, nums):
        a=0
        b=0
        for i in nums:
            a+=i
            b+=sum(map(int,str(i)))
        return abs(a-b)