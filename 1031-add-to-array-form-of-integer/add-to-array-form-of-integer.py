class Solution(object):
    def addToArrayForm(self, num, k):
        n=int("".join(map(str,num)))
        # n=n+k
        return list(map(int,str(n+k)))