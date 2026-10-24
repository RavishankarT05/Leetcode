class Solution(object):
    def canAliceWin(self, n):
        stone=10
        count=0
        while n>=stone:
            n-=stone
            stone-=1
            count+=1
        return count%2==1
        