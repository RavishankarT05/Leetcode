class Solution(object):
    def digitFrequencyScore(self, n):
        l=list(map(int,str(n)))
        return sum(l)