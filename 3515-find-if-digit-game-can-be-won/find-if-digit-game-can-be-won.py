class Solution(object):
    def canAliceWin(self, nums):
        a,b=0,0
        for i in nums:
            if 0<i<10:
                a+=i
            else:
                b+=i
        return a!=b