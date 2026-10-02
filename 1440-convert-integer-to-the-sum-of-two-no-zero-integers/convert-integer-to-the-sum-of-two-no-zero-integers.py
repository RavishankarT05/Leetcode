class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1,n+1):
            w=list(map(int,str(i)))
            q=list(map(int,str(n-i)))
            if n-i!=0 and 0 not in q and 0 not in w:
                return [i,n-i]
