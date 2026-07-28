class Solution(object):
    def repeatedNTimes(self, nums):
        count=0
        a=0
        b=set(nums)
        for i in b:
            c=nums.count(i)
            if count<c:
                count=c
                a=i
        return a
        