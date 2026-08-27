class Solution(object):
    def repeatedNTimes(self, nums):
        b=[]
        for i in nums:
            if i in b:
                return i
            b.append(i)