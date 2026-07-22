class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a=[]
        count=0
        for i in nums:
            for j in nums:
                if i>j:
                    count+=1
            a.append(count)
            count=0
        return a