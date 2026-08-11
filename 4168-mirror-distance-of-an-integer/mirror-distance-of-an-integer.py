class Solution(object):
    def mirrorDistance(self, n):
        a=int(str(n)[::-1])
        return abs(n-a)
        