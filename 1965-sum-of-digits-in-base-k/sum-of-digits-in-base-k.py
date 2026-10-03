class Solution(object):
    def sumBase(self, n, k):
        ans=0
        while n>0:
            rem=n%k
            ans+=rem
            n//=k
        return ans