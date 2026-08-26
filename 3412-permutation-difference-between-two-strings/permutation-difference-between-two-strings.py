class Solution(object):
    def findPermutationDifference(self, s, t):
        count=0
        for i in s:
            count+=abs(s.index(i)-t.index(i))
        return count
        