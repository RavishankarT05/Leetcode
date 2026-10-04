class Solution(object):
    def decimalRepresentation(self, n):
        n=list(map(int,str(n)))
        a=[]
        b=0
        for i in range(len(n)-1,0,-1):
            for j in range(i):
                n[b]=n[b]*10
            b+=1
        c=n.count(0)
        for i in range(c):
            n.remove(0)
        return n
        