class Solution:
    def findRelativeRanks(self, nums):
        a=[]
        s=sorted(nums,reverse=True)
        for i in nums:
            if s.index(i)==0:
                a.append("Gold Medal")
            elif s.index(i)==1:
                a.append("Silver Medal")
            elif s.index(i)==2:
                a.append("Bronze Medal")
            else:
                a.append(str(s.index(i)+1))
        return a