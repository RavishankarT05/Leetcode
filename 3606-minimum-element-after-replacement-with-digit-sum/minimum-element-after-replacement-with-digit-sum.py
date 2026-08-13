class Solution(object):
    def minElement(self, nums):
        a=[]
        for i in nums:
            a.append(sum(map(int,str(i))))
        a.sort()
        return a[0]
        