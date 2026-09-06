class Solution(object):
    def alternateDigitSum(self, n):
        n=list(map(int,str(n)))
        a=[]
        b=[]
        for i in range(0,len(n),2):
            a.append(n[i])
        for i in range(1,len(n),2):
            b.append(n[i])
        return sum(a)-sum(b)