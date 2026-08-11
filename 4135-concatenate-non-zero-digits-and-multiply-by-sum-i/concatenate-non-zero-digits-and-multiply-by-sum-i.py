class Solution(object):
    def sumAndMultiply(self, n):
        if n==0:
            return 0
        a=[]
        for i in (str(n)):
            if int(i)!=0:
                a.append(int(i))
        c=int(''.join(map(str,a)))
        return sum(a)*c


        