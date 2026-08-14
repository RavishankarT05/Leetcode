class Solution(object):
    def limitOccurrences(self, nums, k):
        a=[]
        for i in nums:
            if a.count(i)<k:
                a.append(i)
        return a