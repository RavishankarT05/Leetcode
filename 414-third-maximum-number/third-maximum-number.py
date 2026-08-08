class Solution(object):
    def thirdMax(self, nums):
        b=sorted(set(nums),reverse=True)
        print(b)
        a=len(b)
        if a>=3:
            return b[2]
        elif a==2:
            return b[0]
        else:
            return b[0]
        