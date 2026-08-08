class Solution(object):
    def thirdMax(self, nums):
        b=sorted(set(nums),reverse=True)
        a=len(b)
        if a>=3:
            return b[2]
        else:
            return b[0]
        