class Solution(object):
    def checkDivisibility(self, n):
        num=list(map(int,str(n)))
        a=sum(num)
        b=1
        for i in num:
            b*=i
        if n%(a+b)==0:
            return True
        return False
        