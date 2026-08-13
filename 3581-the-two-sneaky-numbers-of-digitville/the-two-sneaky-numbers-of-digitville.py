class Solution(object):
    def getSneakyNumbers(self, nums):
        a=[]
        num=list(set(nums))
        for i in num:
            if nums.count(i)==2:
                a.append(i)
        return a