class Solution(object):
    def alternateDigitSum(self, n):
        n=list(map(int,str(n)))
        a=[]
        b=[]
        for i in range(len(n)):
            if i%2==0:
                a.append(n[i])
            else:
                b.append(n[i])
        return sum(a)-sum(b)