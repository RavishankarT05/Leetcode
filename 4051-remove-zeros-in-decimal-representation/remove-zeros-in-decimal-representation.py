class Solution(object):
    def removeZeros(self, n):
        n=list(map(int,str(n)))
        a=[]
        for i in n:
            if i!=0:
                a.append(i)
        n=int(''.join(map(str,a)))
        return n