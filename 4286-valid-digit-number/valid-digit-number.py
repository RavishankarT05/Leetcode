class Solution(object):
    def validDigit(self, n, x):
        n=list(map(int,str(n)))
        if x in n:
            if n[0]==x:
                return False
            return True
        return False
        