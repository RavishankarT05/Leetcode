class Solution(object):
    def checkGoodInteger(self, n):
        a=list(map(int,str(n)))
        b=list(map(int,str(n)))
        b=[num ** 2 for num in b]
        return sum(b)-sum(a)>=50
        